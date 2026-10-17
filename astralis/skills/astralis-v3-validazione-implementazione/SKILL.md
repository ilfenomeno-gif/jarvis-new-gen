---
name: "astralis-v3-validazione-implementazione"
description: "Verifica un risultato già realizzato rispetto a requisiti, contratti e prove di accettazione. Non usare per: Giudizio su una strategia astratta, piano non eseguito o sola ricerca di bug nel diff."
metadata: {"id": "AST-S-VALIDAZIONE-IMPLEMENTAZIONE", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "04_validazione_ed_esecuzione", "protocols": [2], "intents": ["validare_implementazione"], "use_when": ["Verifica un risultato già realizzato rispetto a requisiti, contratti e prove di accettazione."], "avoid_when": ["Giudizio su una strategia astratta, piano non eseguito o sola ricerca di bug nel diff."], "materials": ["Implementazione o artefatto, requisiti e ambiente di verifica disponibile."], "prompt_ids": ["AST-P-VALIDAZIONE-IMPLEMENTAZIONE"], "sources": []}
---

# Validazione dell’implementazione

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Implementazione o artefatto, requisiti e ambiente di verifica disponibile.

Non applicare per: Giudizio su una strategia astratta, piano non eseguito o sola ricerca di bug nel diff.

## Metodo

- Per i fix verifica riproduzione originale, eliminazione della causa e conservazione dell’invariante nei percorsi correlati; controlla proprietà dello stato e confini modificati. Per moduli nuovi valuta contratti, dipendenze e isolamento pertinente. Una preferenza architetturale non basta per un verdetto negativo e una suite superata non dimostra da sola il comportamento di un’AI.
- Associa requisiti e comportamenti osservabili, includendo accessibilità quando pertinente.
- Seleziona controlli proporzionati al rischio e usa soltanto strumenti e ambienti disponibili.
- Distingui verificato, fallito e non verificabile, conservando evidenze e comandi effettivi.
- Non equiparare un test unitario superato a un collaudo completo. Correzioni e deploy seguono il mandato già disponibile.
- Applica la matrice Astralis: validità, efficacia, coerenza, completezza, precisione per NVDA, affidabilità/prestazioni e assenza di regressioni; considera uso comune, percorsi alternativi e casi limite. Distingui simulazione e prova eseguita, dichiarando gli assi non verificabili o non applicabili.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
