---
name: "astralis-v3-strategia-logica"
description: "Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito. Non usare per: Validazione di una strategia già fornita, piano tecnico dettagliato o hotfix semplice con causa e soluzione note."
metadata: {"id": "AST-S-STRATEGIA-LOGICA", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "02_decisione_e_pianificazione", "protocols": [1, 12], "intents": ["creare_strategia_logica"], "use_when": ["Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito."], "avoid_when": ["Validazione di una strategia già fornita, piano tecnico dettagliato o hotfix semplice con causa e soluzione note."], "materials": ["Problema, obiettivo, contesto e vincoli; evidenze o idea di origine se presenti."], "prompt_ids": ["AST-P-STRATEGIA-LOGICA"], "sources": []}
---

# Redazione di una strategia logica

## Ambito e materiali

Metodo del catalogo Astralis 3.X. Problema, obiettivo, contesto e vincoli; evidenze o idea di origine se presenti.
Rispetta il mandato già espresso, le istruzioni attive e l’accessibilità NVDA; la selezione non concede nuovi permessi. Questo metodo non dipende da Astralis 4.

## Metodo

- Nel modello concettuale chiarisci confini dei domini, responsabilità e proprietà dello stato condiviso. Valuta indipendenza e integrazione senza imporre un hub globale; rimanda contratti tecnici e classi al piano. La modularità deve essere proporzionata al bisogno.
- Definisci dilemma, comportamento desiderato e modello mentale dal punto di vista di utente e sistema. Prima considera capacità native, configurazione e riuso.
- Scegli un archetipo pertinente: concettuale, diagnostico, refactoring, accessibilità, dialettico, interoperabilità o migrazione. Non trasformarlo in sette processi obbligatori.
- Confronta soltanto alternative plausibili e motiva la tesi proposta; separa ipotesi da decisioni già convalidate.
- Definisci invarianti concettuali e rischi negli scenari comuni, alternativi e limite. Applica i sei cancelli nelle dimensioni pertinenti, senza imporre input fisico o hitbox a un’API.
- Registra punti aperti, convergenza preliminare e invarianti convalidate con fonte reale della decisione. Contratti D/S dettagliati, patch e sequenze esecutive appartengono al piano.
- Concludi con criterio di conversione e prossimo passo. Se la persistenza è utile e compresa nel mandato usa STRATEGIA_COGNITIVA_TEMPLATE.md nella radice documentale. Se una strategia è già fornita per un giudizio, usare validazione-strategia; nessuna implementazione implicita.

## Raccordo

Il prompt nei metadati è una forma esplicita di incarico, non una dipendenza obbligatoria. Se il Master Hub v3 è accessibile consulta la mappa ciclo_sviluppo_e_selezione_strumenti_astralis.md e la tassonomia nella knowledge di architettura per i dettagli pertinenti. Questo SKILL.md contiene il metodo essenziale; non fingere strumenti o letture non disponibili.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/clean_architecture_e_design_pattern.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
