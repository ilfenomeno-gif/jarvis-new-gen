---
name: "astralis-v3-continuita-sessione"
description: "Prepara ripresa, sospensione o handoff di un’iniziativa conservando stato, evidenze, vincoli e prossimo passo tra sessioni o AI. Non usare per: Normale risposta conclusiva senza necessità di ripresa o invio automatico a un’altra AI."
metadata: {"id": "AST-S-CONTINUITA-SESSIONE", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [6, 7], "intents": ["preservare_continuita_sessione"], "use_when": ["Prepara ripresa, sospensione o handoff di un’iniziativa conservando stato, evidenze, vincoli e prossimo passo tra sessioni o AI."], "avoid_when": ["Normale risposta conclusiva senza necessità di ripresa o invio automatico a un’altra AI."], "materials": ["Iniziativa, report o RRU pertinente, stato corrente, mandato e attività aperte."], "prompt_ids": [], "sources": []}
---

# Continuità di sessione e passaggio di consegne

## Ambito e materiali

Metodo Astralis 3.X. Iniziativa, report o RRU pertinente, stato corrente, mandato e attività aperte.
Rispetta il mandato già dato e gli ingressi attivi. Non dipende da Astralis 4; mantiene output lineare NVDA e non conferisce permessi ulteriori.

## Metodo

- Alla ripresa recupera dal report pertinente ultimo stato datato ed esito; verifica i riferimenti correnti prima di continuare.
- Alla sospensione o consegna aggiorna il report esistente con lavoro svolto, ambiente, blocchi, materiali e prossimo passo. Evita un nuovo file quando non aggiunge identità o perimetro.
- Usa intento COORDINAMENTO-CHIUSURA per un handoff; separa raccomandazione, decisione ratificata e mandato residuo con riferimento alla richiesta reale dell’utente.
- Separa completamento tecnico, verifica e convalida finale; non chiudere la revisione perché è terminata la chat.
- Conserva contributi e cronologia, designando un curatore se più AI scrivono. Un documento di consegna non autorizza messaggi ad altre chat, deleghe o pubblicazione.

## Raccordo con Astralis

Se il Master Hub v3 è accessibile, consulta la procedura gestione_report_e_continuita_sessioni.md nella knowledge di architettura quando servono dettagli; per nuovi report usa templates/REPORT_SESSIONE_TEMPLATE.md e la tassonomia attiva. Questa scheda contiene il metodo essenziale. Non fingere letture o strumenti non disponibili.
