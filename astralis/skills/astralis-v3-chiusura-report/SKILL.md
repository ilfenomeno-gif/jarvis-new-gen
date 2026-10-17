---
name: "astralis-v3-chiusura-report"
description: "Verifica e archivia report nel ciclo di chiusura autorizzato con esito convalidato, preservando storia e puntatori documentali. Non usare per: Sola lettura, singolo test verde, iniziativa ancora aperta o migrazione retroattiva degli archivi."
metadata: {"id": "AST-S-CHIUSURA-REPORT", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [6], "intents": ["chiudere_report"], "use_when": ["Verifica e archivia report nel ciclo di chiusura autorizzato con esito convalidato, preservando storia e puntatori documentali."], "avoid_when": ["Sola lettura, singolo test verde, iniziativa ancora aperta o migrazione retroattiva degli archivi."], "materials": ["Mandato di chiusura, convalida richiesta, report e documenti che lo referenziano."], "prompt_ids": [], "sources": []}
---

# Chiusura e archiviazione coerente dei report

## Ambito e materiali

Metodo Astralis 3.X. Mandato di chiusura, convalida richiesta, report e documenti che lo referenziano.
Rispetta il mandato già dato e gli ingressi attivi. Non dipende da Astralis 4; mantiene output lineare NVDA e non conferisce permessi ulteriori.

## Metodo

- Verifica che convalida e mandato riguardino proprio l’iniziativa e le prove richieste; un completamento tecnico non basta per una chiusura runtime.
- Ricostruisci report, RRU, piano, strategia e allegati realmente interessati senza imporre nodi assenti. Controlla destinazione, collisioni e collegamenti in entrata.
- Preserva originale, ID, autori ed evidenze. Non sovrascrivere un file omonimo né riscrivere archivi storici; per rettifiche crea un nuovo documento collegato.
- Nel perimetro autorizzato trasferisci e aggiorna i puntatori relativi interessati; verifica esistenza e riferimenti prima di dichiarare concluso il ciclo. Se una parte è bloccata non dichiarare archiviazione completa.
- Riassumi la chiusura con link canonici e questioni residue. Non includere commit, push, cancellazioni o release che il mandato non autorizza.

## Raccordo con Astralis

Se il Master Hub v3 è accessibile, consulta la procedura gestione_report_e_continuita_sessioni.md nella knowledge di architettura quando servono dettagli; per nuovi report usa templates/REPORT_SESSIONE_TEMPLATE.md e la tassonomia attiva. Questa scheda contiene il metodo essenziale. Non fingere letture o strumenti non disponibili.
