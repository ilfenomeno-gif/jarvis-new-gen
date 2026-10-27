import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys

MAX_PLAN_TASKS = 5
MAX_RESEARCH_WORKERS = 3
MAX_RESEARCH_RESULT_CHARS = 3000


def get_base_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent

BASE_DIR = get_base_dir()
API_CONFIG_PATH = BASE_DIR / "config" / "api_keys.json"

def _get_api_key() -> str:
    from core.api_keys import gemini_api_key
    return gemini_api_key(API_CONFIG_PATH.parent)

def _get_model(model_name: str = "gemini-flash-latest"):
    from google import genai
    import time
    _c = genai.Client(api_key=_get_api_key())
    class _W:
        def generate_content(self, contents):
            return _c.models.generate_content(model=model_name, contents=contents)
    return _W()

def run_supervisor(task_description: str) -> dict:
    """
    Supervisor Agent analyzes the task and breaks it down into subtasks for other agents.
    Returns a planned workflow dict.
    """
    task_description = (task_description or "").strip()
    if not task_description:
        return {"error": "A non-empty task is required.", "plan_summary": ""}
    if len(task_description) > 12_000:
        return {"error": "Task description exceeds 12000 characters.", "plan_summary": ""}

    model = _get_model()
    prompt = f"""You are the Supervisor Agent of a multi-agent AI coding system.
Analyze the following user task and break it down into steps for the sub-agents:
1. Research Agent: to search documentation and APIs.
2. Coder Agent: to write code.
3. Debugger Agent: to test and fix the code.

Task: {task_description}

Return ONLY valid JSON with this structure:
{{
    "plan_summary": "Brief summary",
    "research_tasks": ["search for X", "check Y"],
    "coding_tasks": ["create module Z", "implement function W"],
    "testing_tasks": ["run tests on Z", "verify W"]
}}
"""
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        text = re.sub(r"^```[a-zA-Z]*\r?\n?", "", text)
        text = re.sub(r"\r?\n?```\s*$", "", text)
        plan = json.loads(text.strip())
        if not isinstance(plan, dict):
            raise ValueError("The supervisor response must be a JSON object.")
        for field in ("research_tasks", "coding_tasks", "testing_tasks"):
            tasks = plan.get(field, [])
            if not isinstance(tasks, list):
                raise ValueError(f"{field} must be a list.")
            if any(not isinstance(item, str) for item in tasks):
                raise ValueError(f"{field} may contain only strings.")
            plan[field] = [
                item.strip()[:1000]
                for item in tasks[:MAX_PLAN_TASKS]
                if item.strip()
            ]
        summary = plan.get("plan_summary", "")
        if not isinstance(summary, str):
            raise ValueError("plan_summary must be a string.")
        plan["plan_summary"] = summary.strip()[:1000]
        return plan
    except Exception as e:
        return {"error": str(e), "plan_summary": "Failed to parse plan"}


def _execute_research(tasks: list[str]) -> list[dict]:
    if not tasks:
        return []

    from agents.research_agent import run_research

    def run(task: str) -> dict:
        try:
            result = run_research(task)
            failed = result.startswith("Research error:")
            return {
                "task": task,
                "status": "failed" if failed else "completed",
                "result": result[:MAX_RESEARCH_RESULT_CHARS],
            }
        except Exception as exc:
            return {"task": task, "status": "failed", "error": str(exc)}

    with ThreadPoolExecutor(
        max_workers=min(MAX_RESEARCH_WORKERS, len(tasks))
    ) as executor:
        return list(executor.map(run, tasks))


def supervisor_action(parameters: dict, **kwargs) -> str:
    task = parameters.get("task", "")
    if not task:
        return "Supervisor needs a task."
    plan = run_supervisor(task)
    if "error" not in plan:
        plan["research_results"] = _execute_research(plan.get("research_tasks", []))
        plan["handoff"] = {
            "coding": (
                "Not executed; code generation requires a separate user-directed "
                "coder_agent call and an approved destination."
            ),
            "testing": (
                "Not executed; commands require a separate user-directed "
                "debugger_agent call and explicit confirmation."
            ),
        }
    return json.dumps(plan, indent=2)
