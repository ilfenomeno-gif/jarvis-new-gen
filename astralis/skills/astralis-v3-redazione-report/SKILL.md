---
name: "astralis-v3-redazione-report"
description: "Crea o aggiorna report da evidenze reali durante lavoro sostanziale autorizzato, diagnosi, collaudo o consegna che richiedono continuità, anche senza richiesta separata di report. Non usare per: Chiarimenti banali, nessun avanzamento o analisi consultiva priva di mandato di salvataggio."
metadata: {"id": "AST-S-REDAZIONE-REPORT", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [4, 6, 7], "intents": ["redigere_report"], "use_when": ["Crea o aggiorna report da evidenze reali durante lavoro sostanziale autorizzato, diagnosi, collaudo o consegna che richiedono continuità, anche senza richiesta separata di report."], "avoid_when": ["Chiarimenti banali, nessun avanzamento o analisi consultiva priva di mandato di salvataggio."], "materials": ["Obiettivo, mandato, radice documentale risolta, attività ed evidenze effettive."], "prompt_ids": [], "sources": ["skill-report-writer.md"]}
---

# Redazione e aggiornamento dei report

## Ambito e materiali

Metodo Astralis 3.X. Obiettivo, mandato, radice documentale risolta, attività ed evidenze effettive.
Rispetta il mandato già dato e gli ingressi attivi. Non dipende da Astralis 4; mantiene output lineare NVDA e non conferisce permessi ulteriori.

## Metodo

- Risolvi separatamente repository codice, documentazione e runtime; riusa il report pertinente senza creare registri nel checkout sbagliato.
- Per nuovi report usa la Testata Universale Compatta: ID, tipo REPORT, intento, ambito, stato documento, stato lavoro, gate ed evidenza, partecipanti reali, modalità, documenti correlati, Git e ultimo aggiornamento. Non inventare metadati; conserva testate legacy nei documenti storici.
- Metti subito dopo metadati e obiettivo stato datato, prossimo passo e limite; registra attività svolte, evidenze, risultati, esito verifiche, decisioni e limiti. Gli aggiornamenti significativi più recenti precedono quelli storici.
- Distingui analisi, test automatici, build, deploy e prova runtime/NVDA. Riporta comandi, contesto, SHA quando pertinente e risultati effettivi; NON ESEGUITE o PARZIALI non sono fallimenti inventati né PASS.
- Prima di scrivere rileggi l’ultimo contenuto e conserva contributi altrui. Aggiorna per eventi significativi senza duplicare diagnosi in RRU e piano; usa allegati per dump utili mantenendo provenienza e dettagli.
- La documentazione interna necessaria al lavoro autorizzato segue il mandato già dato, senza conferme duplicate. Una richiesta di soli consigli non autorizza invii, pubblicazione, deploy o cambiamenti ulteriori. Non archiviare un’iniziativa aperta.

## Raccordo con Astralis

Se il Master Hub v3 è accessibile, consulta la procedura gestione_report_e_continuita_sessioni.md nella knowledge di architettura quando servono dettagli; per nuovi report usa templates/REPORT_SESSIONE_TEMPLATE.md e la tassonomia attiva. Questa scheda contiene il metodo essenziale. Non fingere letture o strumenti non disponibili.
