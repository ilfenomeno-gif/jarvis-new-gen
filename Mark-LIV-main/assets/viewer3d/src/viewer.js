import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const state = {
  markers: [], target: null, spin: true, ready: false, flights: null,
  model: null, modelStatus: "none", modelError: "", shaderError: "", partInfo: {},
  style: "hologram",
};
const canvas = document.getElementById("c");
// Senza WebGL (GPU in blocklist) il viewer resta controllabile ma non disegna.
let renderer = null;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setClearColor(0x000308, 1);
  renderer.debug.onShaderError = () => { state.shaderError = "shader compile failed"; };
} catch (e) {
  console.error("WebGL non disponibile: " + e.message);
}
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
camera.position.set(0, 0, 4.2);

const globe = new THREE.Group();
scene.add(globe);
const cyan = 0x00d4ff;

// Only the solid styles (blueprint, realistic) are lit; globe and hologram are unlit.
scene.add(new THREE.HemisphereLight(0xcfe8ff, 0x10203a, 1.6));
const keyLight = new THREE.DirectionalLight(0xffffff, 2.4);
keyLight.position.set(2, 3, 4);
scene.add(keyLight);

const sphere = new THREE.Mesh(
  new THREE.SphereGeometry(1, 48, 32),
  new THREE.MeshBasicMaterial({ color: cyan, wireframe: true, transparent: true, opacity: 0.18 })
);
globe.add(sphere);
globe.add(new THREE.Mesh(
  new THREE.SphereGeometry(0.985, 32, 24),
  new THREE.MeshBasicMaterial({ color: 0x001018, transparent: true, opacity: 0.85 })
));

const rings = [];
for (let i = 0; i < 3; i++) {
  const ring = new THREE.Mesh(
    new THREE.RingGeometry(1.25 + i * 0.12, 1.26 + i * 0.12, 128),
    new THREE.MeshBasicMaterial({ color: cyan, transparent: true, opacity: 0.35 - i * 0.08, side: THREE.DoubleSide })
  );
  ring.rotation.x = Math.PI / 2.3 + i * 0.25;
  scene.add(ring);
  rings.push(ring);
}

function toVec(lat, lon, r) {
  const phi = (90 - lat) * Math.PI / 180;
  const theta = (lon + 180) * Math.PI / 180;
  return new THREE.Vector3(
    -r * Math.sin(phi) * Math.cos(theta),
    r * Math.cos(phi),
    r * Math.sin(phi) * Math.sin(theta)
  );
}

function resize() {
  const w = canvas.clientWidth || 1, h = canvas.clientHeight || 1;
  if (renderer) renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}
window.addEventListener("resize", resize);

// Rotation that brings (lat, lon) to face the camera (+z).
function rotationFor(lat, lon) {
  const target = toVec(lat, lon, 1).normalize();
  return new THREE.Quaternion().setFromUnitVectors(target, new THREE.Vector3(0, 0, 1));
}

let last = performance.now();
function frame(now) {
  const dt = Math.min(0.1, (now - last) / 1000);
  last = now;
  if (state.target) {
    globe.quaternion.slerp(state.target, Math.min(1, dt * 3));
    if (globe.quaternion.angleTo(state.target) < 0.005) {
      globe.quaternion.copy(state.target);
    }
  } else if (state.spin) {
    globe.rotation.y += dt * 0.25;
  }
  rings.forEach((r, i) => { r.rotation.z += dt * (0.2 + i * 0.1); });
  if (state.model && state.model.holo.length) {
    state.model.holo.forEach(m => { m.uniforms.uTime.value = now / 1000; });
  }
  if (state.model && state.spin) state.model.group.rotation.y += dt * 0.4;
  if (state.model && state.model.parts.length) {
    const m = state.model;
    m.explode += (m.explodeTo - m.explode) * Math.min(1, dt * 4);
    if (Math.abs(m.explodeTo - m.explode) < 0.002) m.explode = m.explodeTo;
    m.parts.forEach(p => p.node.position.copy(p.origin).addScaledVector(p.dir, p.dist * m.explode));
  }
  pickPart(now);
  if (renderer) renderer.render(scene, camera);
  requestAnimationFrame(frame);
}

function num(v, lo, hi, name) {
  const n = Number(v);
  if (!Number.isFinite(n) || n < lo || n > hi) throw new Error(name + " out of range");
  return n;
}

// Parts are the first level of nodes that actually splits the model.
function collectParts(root, size) {
  let level = [root];
  for (let i = 0; i < 6; i++) {
    const next = level.flatMap(o => o.children);
    if (next.length === 0) return [];
    if (next.length > 1) { level = next; break; }
    level = next;
  }
  if (level.length < 2) return [];
  // A split into just two chunks is a poor explosion: open up to three more levels.
  for (let k = 0; k < 3 && level.length < 3; k++) {
    const deeper = level.flatMap(o => (o.children.length ? o.children : [o]));
    if (deeper.length === level.length) break;
    level = deeper;
  }
  const all = new THREE.Box3().setFromObject(root).getCenter(new THREE.Vector3());
  return level.map((node, i) => {
    const c = new THREE.Box3().setFromObject(node).getCenter(new THREE.Vector3());
    const dir = node.parent.worldToLocal(c).sub(node.parent.worldToLocal(all.clone()));
    if (dir.lengthSq() < 1e-8) dir.set(Math.cos(i * 2.4), Math.sin(i * 2.4), 0.3);
    return { node, origin: node.position.clone(), dir: dir.normalize(), dist: size * 0.6, saved: null };
  });
}

function findNode(root, name) {
  let hit = null;
  root.traverse(o => { if (!hit && o.name === name) hit = o; });
  return hit;
}

const HOLO_COLOR = 0x00d4ff;
const HOLO_VERT = `
varying vec3 vNormal; varying vec3 vView; varying float vY;
void main() {
  vec4 mv = modelViewMatrix * vec4(position, 1.0);
  vNormal = normalize(normalMatrix * normal);
  vView = normalize(-mv.xyz);
  vY = (modelMatrix * vec4(position, 1.0)).y;
  gl_Position = projectionMatrix * mv;
}`;
const HOLO_FRAG = `
uniform vec3 uColor; uniform float uTime;
varying vec3 vNormal; varying vec3 vView; varying float vY;
void main() {
  float fres = pow(1.0 - abs(dot(normalize(vNormal), normalize(vView))), 2.0);
  float scan = 0.55 + 0.45 * sin(vY * 90.0 - uTime * 3.0);
  float glitch = step(0.985, fract(sin(floor(uTime * 8.0) + floor(vY * 20.0)) * 43758.5453));
  float a = (0.22 + fres * 0.75) * scan + glitch * 0.3;
  gl_FragColor = vec4(uColor * (0.7 + fres), a);
}`;

function holoMaterial() {
  return new THREE.ShaderMaterial({
    uniforms: { uColor: { value: new THREE.Color(HOLO_COLOR) }, uTime: { value: 0 } },
    vertexShader: HOLO_VERT,
    fragmentShader: HOLO_FRAG,
    transparent: true,
    depthWrite: false,
    side: THREE.DoubleSide,
    blending: THREE.AdditiveBlending,
  });
}

const BLUEPRINT_COLOR = 0x0055ff;
const EDGE_COLOR = 0x00f0ff;
const STYLES = ["hologram", "blueprint", "realistic"];

function meshesOf(root) {
  const list = [];
  root.traverse(o => { if (o.isMesh) list.push(o); });
  return list;
}

function blueprintMaterial() {
  return new THREE.MeshStandardMaterial({
    color: BLUEPRINT_COLOR, roughness: 0.8, metalness: 0.2, side: THREE.DoubleSide,
    // Pushes the faces back so the edge lines do not z-fight with them.
    polygonOffset: true, polygonOffsetFactor: 1, polygonOffsetUnits: 1,
  });
}

// Callers clear any glow first: this swaps the materials the glow clones from.
function applyStyle(model, style) {
  model.holo = [];
  model.meshes.forEach(o => {
    if (o.userData.base) {
      o.material.dispose();
      o.material = o.userData.base;
      delete o.userData.base;
      delete o.userData.holo;
      delete o.userData.glow;
    }
    if (o.userData.edgeLines) {
      const lines = o.userData.edgeLines;
      o.remove(lines);
      lines.geometry.dispose();
      lines.material.dispose();
      delete o.userData.edgeLines;
    }
    if (style === "hologram") {
      if (!o.geometry.attributes.normal) o.geometry.computeVertexNormals();
      o.userData.base = o.material;
      o.material = holoMaterial();
      o.userData.holo = true;
      model.holo.push(o.material);
    } else if (style === "blueprint") {
      o.userData.base = o.material;
      o.material = blueprintMaterial();
      const lines = new THREE.LineSegments(
        new THREE.EdgesGeometry(o.geometry, 45),
        new THREE.LineBasicMaterial({ color: EDGE_COLOR })
      );
      o.add(lines);
      o.userData.edgeLines = lines;
    }
  });
  model.style = style;
  model.hologram = style === "hologram";
}

// Hover tooltip: raycasting is throttled and only runs when the mouse moved.
const tip = document.getElementById("tip");
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
const hover = { x: 0, y: 0, pending: false, last: 0, rays: 0, name: "", text: "" };
const RAY_INTERVAL_MS = 50;

// The Python side listens to the page console for this prefix (see ui.py).
function emitHover(name, text) {
  console.info("JARVIS_HOVER " + JSON.stringify({ name, text }));
}

function hideTip() {
  if (hover.name) emitHover("", "");
  hover.name = ""; hover.text = "";
  if (tip) tip.style.display = "none";
}

function placeTip() {
  if (!tip) return;
  const w = tip.offsetWidth, h = tip.offsetHeight;
  tip.style.left = Math.max(0, Math.min(hover.x + 14, window.innerWidth - w - 4)) + "px";
  tip.style.top = Math.max(0, Math.min(hover.y + 16, window.innerHeight - h - 4)) + "px";
}

function showTip(name, text) {
  hover.name = name; hover.text = text;
  emitHover(name, text);
  if (!tip) return;
  tip.textContent = "";
  const title = document.createElement("b");
  title.textContent = name;
  tip.appendChild(title);
  if (text) {
    const body = document.createElement("div");
    body.textContent = text;
    tip.appendChild(body);
  }
  tip.style.display = "block";
  placeTip();
}

// Nearest named ancestor (the model root itself is not a part); a described one wins.
function partAt(obj, root) {
  let first = "";
  for (let o = obj; o && o !== root; o = o.parent) {
    if (!o.name) continue;
    if (!first) first = o.name;
    if (Object.prototype.hasOwnProperty.call(state.partInfo, o.name)) {
      return { name: o.name, text: state.partInfo[o.name] };
    }
  }
  if (first) return { name: first, text: "" };
  // Unnamed nodes (e.g. Khronos engine models): label by top-level part.
  const m = state.model;
  const idx = m ? m.parts.findIndex(p => { for (let o = obj; o; o = o.parent) if (o === p.node) return true; return false; }) : -1;
  if (idx >= 0) {
    const key = "Parte " + (idx + 1);
    return { name: key, text: Object.prototype.hasOwnProperty.call(state.partInfo, key) ? state.partInfo[key] : "" };
  }
  return { name: "", text: "" };
}

function pickPart(now) {
  if (!hover.pending || now - hover.last < RAY_INTERVAL_MS) return;
  hover.last = now;
  const m = state.model;
  if (!m || !m.group.visible) { hover.pending = false; hideTip(); return; }
  const rect = canvas.getBoundingClientRect();
  if (!rect.width || !rect.height) return;
  pointer.set(((hover.x - rect.left) / rect.width) * 2 - 1, -((hover.y - rect.top) / rect.height) * 2 + 1);
  scene.updateMatrixWorld();
  camera.updateMatrixWorld();
  raycaster.setFromCamera(pointer, camera);
  hover.rays++;
  const hit = raycaster.intersectObjects(m.meshes, false)[0];
  const part = hit ? partAt(hit.object, m.root) : { name: "", text: "" };
  if (!part.name) { hover.pending = false; hideTip(); return; }
  // While the tooltip is up keep re-testing (a spinning model moves under the cursor).
  if (part.name !== hover.name || part.text !== hover.text) showTip(part.name, part.text);
  else placeTip();
}

canvas.addEventListener("mousemove", (e) => {
  hover.x = e.clientX; hover.y = e.clientY; hover.pending = true;
  if (tip && tip.style.display === "block") placeTip();
});
canvas.addEventListener("mouseleave", () => { hover.pending = false; hideTip(); });

function setGlow(node, on) {
  node.traverse(o => {
    if (!o.isMesh) return;
    if (o.userData.holo) {
      o.userData.glow = on;
      o.material.uniforms.uColor.value.setHex(on ? 0xffd400 : HOLO_COLOR);
      return;
    }
    if (on && !o.userData.orig) {
      o.userData.orig = o.material;
      o.material = [].concat(o.material).map(m => {
        const c = m.clone();
        if (c.emissive) { c.emissive.setHex(0x00d4ff); c.emissiveIntensity = 1.2; }
        else if (c.color) c.color.setHex(0x00d4ff);
        return c;
      });
      if (o.material.length === 1) o.material = o.material[0];
    } else if (!on && o.userData.orig) {
      [].concat(o.material).forEach(m => m.dispose());
      o.material = o.userData.orig;
      delete o.userData.orig;
    }
  });
}

function nodeNames(root) {
  const out = [];
  root.traverse(o => { if (o !== root && o.name) out.push(o.name); });
  return out;
}

window.jarvisViewer = {
  flyTo(lat, lon) {
    state.target = rotationFor(num(lat, -90, 90, "lat"), num(lon, -180, 180, "lon"));
    state.spin = false;
  },
  addMarker(lat, lon, label) {
    lat = num(lat, -90, 90, "lat"); lon = num(lon, -180, 180, "lon");
    const dot = new THREE.Mesh(
      new THREE.SphereGeometry(0.025, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0xffd400 })
    );
    dot.position.copy(toVec(lat, lon, 1.01));
    globe.add(dot);
    state.markers.push({ lat, lon, label: String(label || "").slice(0, 60), obj: dot });
  },
  clearMarkers() {
    state.markers.forEach(m => globe.remove(m.obj));
    state.markers = [];
  },
  setFlights(list) {
    this.clearFlights();
    const pos = new Float32Array(list.length * 3);
    list.forEach((f, i) => toVec(f[0], f[1], 1.02).toArray(pos, i * 3));
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({
      color: 0xffd400, size: 0.028, sizeAttenuation: true, depthTest: true,
    }));
    globe.add(pts);
    state.flights = { obj: pts, list: list.map(f => ({ lat: f[0], lon: f[1], callsign: f[2] })) };
  },
  clearFlights() {
    if (state.flights) { globe.remove(state.flights.obj); state.flights.obj.geometry.dispose(); }
    state.flights = null;
  },
  loadModel(name) {
    this.removeModel();
    state.modelStatus = "loading";
    new GLTFLoader().load(
      "models/" + name.split("/").map(encodeURIComponent).join("/"),
      (gltf) => {
        const root = gltf.scene;
        const box = new THREE.Box3().setFromObject(root);
        const size = box.getSize(new THREE.Vector3());
        const scale = 1.6 / (Math.max(size.x, size.y, size.z) || 1);
        const group = new THREE.Group();
        root.position.sub(box.getCenter(new THREE.Vector3()));
        group.add(root);
        group.scale.setScalar(scale);
        scene.add(group);
        group.updateMatrixWorld(true);
        state.model = { group, root, name, meshes: meshesOf(root), parts: collectParts(root, Math.max(size.x, size.y, size.z) || 1), explode: 0, explodeTo: 0, highlight: "", holo: [], hologram: false, style: "hologram" };
                applyStyle(state.model, state.style);
        state.modelStatus = "ready";
        globe.visible = false;
        rings.forEach(r => { r.visible = false; });
      },
      undefined,
      (err) => { state.modelStatus = "error"; state.modelError = String(err && err.message || err); }
    );
  },
  explodeModel(on) {
    if (state.model) state.model.explodeTo = on ? 1 : 0;
  },
  highlightPart(name) {
    const m = state.model;
    if (!m) return;
    if (m.highlight) { const old = findNode(m.root, m.highlight); if (old) setGlow(old, false); }
    m.highlight = "";
    const node = name ? findNode(m.root, name) : null;
    if (node) { setGlow(node, true); m.highlight = name; }
  },
  setHologram(on) {
    this.setMaterialStyle(on ? "hologram" : "realistic");
  },
  setMaterialStyle(style) {
    style = String(style);
    if (!STYLES.includes(style)) throw new Error("style must be one of " + STYLES.join(", "));
    state.style = style;
    const m = state.model;
    if (!m) return;
    const keep = m.highlight;
    if (keep) this.highlightPart("");
    applyStyle(m, style);
    if (keep) this.highlightPart(keep);
  },
  setPartInfo(info) {
    const out = {};
    if (info && typeof info === "object" && !Array.isArray(info)) {
      Object.entries(info).slice(0, 200).forEach(([k, v]) => { out[String(k).slice(0, 60)] = String(v).slice(0, 300); });
    }
    state.partInfo = out;
    hover.pending = true;
  },
  clearModel() {
    this.removeModel();
    state.partInfo = {};
  },
  removeModel() {
    if (state.model) {
      scene.remove(state.model.group);
      state.model.root.traverse(o => {
        if (o.geometry) o.geometry.dispose();
        [].concat(o.material || []).forEach(m => m.dispose());
        if (o.userData && o.userData.base) [].concat(o.userData.base).forEach(m => m.dispose());
      });
    }
    state.model = null;
    state.modelStatus = "none";
    state.modelError = "";
    hover.pending = false;
    hideTip();
    globe.visible = true;
    rings.forEach(r => { r.visible = true; });
  },
  spin(on) { state.spin = !!on; if (on) state.target = null; },
  getState() {
    return {
      ready: state.ready,
      webgl: !!renderer,
      flights: state.flights ? state.flights.list.length : 0,
      model: {
        status: state.modelStatus,
        name: state.model ? state.model.name : "",
        error: state.modelError,
        nodes: state.model ? nodeNames(state.model.root) : [],
        parts: state.model ? state.model.parts.length : 0,
        explode: state.model ? Number(state.model.explode.toFixed(3)) : 0,
        moved: state.model ? state.model.parts.map(p => Number(p.node.position.distanceTo(p.origin).toFixed(3))) : [],
        highlight: state.model ? state.model.highlight : "",
        glowing: state.model ? (() => { let n = 0; state.model.root.traverse(o => { if (o.userData.orig || o.userData.glow) n++; }); return n; })() : 0,
        hologram: state.model ? state.model.hologram : false,
        style: state.model ? state.model.style : "",
        edges: state.model ? state.model.meshes.filter(o => o.userData.edgeLines).length : 0,
        meshColors: state.model ? state.model.meshes.map(o => [].concat(o.material)[0].color ? [].concat(o.material)[0].color.getHexString() : "") : [],
        partInfo: Object.keys(state.partInfo).length,
        pendingStyle: state.style,
        hover: { name: hover.name, text: hover.text, rays: hover.rays, visible: !!tip && tip.style.display === "block" },
        shaderError: state.shaderError,
      },
      spin: state.spin,
      flying: !!state.target,
      markers: state.markers.map(m => ({ lat: m.lat, lon: m.lon, label: m.label })),
    };
  },
};

resize();
state.ready = true;
const boot = document.getElementById("boot");
if (boot) {
  if (renderer) boot.remove();
  else boot.textContent = "WebGL non disponibile";
}
requestAnimationFrame(frame);
