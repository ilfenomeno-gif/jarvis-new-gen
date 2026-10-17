# Standard delle skill Astralis 3.X

Revisione del catalogo: 1.3.0. Questo documento riguarda il confezionamento v3, non il rilascio del framework.

## Struttura

Una cartella `astralis-v3-nome` contiene `SKILL.md`. Il frontmatter YAML usa valori JSON, che sono anche YAML validi: permette la verifica con la libreria standard Python senza dipendenze aggiuntive.
I campi principali sono `name`, `description` e `metadata`. Descrizione e confini devono permettere la selezione prima di leggere il corpo. Il corpo contiene il metodo; riferimenti, script e asset si aggiungono solo per un bisogno concreto.

`metadata` contiene ID `AST-S-*`, revisione indipendente, ambito `ASTRALIS 3.X`, categoria, numeri dei protocolli, intenti, condizioni d'uso, esclusioni, materiali, ID dei prompt complementari e nomi delle sorgenti storiche. Liste vuote sono ammesse per prompt e sorgenti quando non esistono corrispondenze; non per i criteri di selezione.

Le categorie organizzano il catalogo e i metadati; non annidare le cartelle delle skill. Gli ID sono stabili: una correzione del metodo cambia la revisione, non l'identità. Non rinumerare i protocolli ufficiali.

## Adattamento

Conservare la capacità utile della sorgente e documentarne la provenienza. Rimuovere convenzioni SPARK dal metodo generale; applicarle soltanto quando richieste dal progetto. Preservare modularità, conoscenza incrementale, accessibilità NVDA e output lineare.
Non imporre quantità di alternative o rilievi, autovalutazioni perfette o deleghe ad altre AI. Non trasformare selezione implicita in permesso implicito. Non eseguire un prompt solo perché è stato creato o revisionato.

Le skill contengono il metodo operativo; i prompt sono forme esplicite di incarico e i loro ID sono collegamenti semantici. Se in futuro le procedure divergono, confrontarle e correggere intenzionalmente entrambe: l'indice verifica i riferimenti, non dimostra equivalenza semantica.

## Modello per una nuova scheda

Usare questo esempio di struttura e sostituire i valori con una capacità reale. Non creare cartelle vuote o skill di esempio nel catalogo attivo.

```yaml
---
name: "astralis-v3-capacita"
description: "Capacità precisa e contesto che ne richiede l'utilizzo."
metadata: {"id": "AST-S-CAPACITA", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "categoria_pertinente", "protocols": [1], "intents": ["intento_specifico"], "use_when": ["Condizione concreta"], "avoid_when": ["Compito vicino da escludere"], "materials": ["Input decisivo"], "prompt_ids": [], "sources": []}
---
```

Nel corpo indicare scopo e limiti, materiali, metodo, evidenze e condizioni di arresto pertinenti. Istruzioni tecnologiche approfondite appartengono alla conoscenza pertinente o a riferimenti confezionati con la skill, senza percorsi assoluti privati.

## Controlli

Rigenerare `INDICE_SELEZIONE.json` dopo modifiche. Usare `--check` per rilevare un indice obsoleto; `--source-root` per confrontare le sorgenti con gli hash registrati. Verificare YAML e nome anche con `quick_validate.py` della skill-creator, quando disponibile.
Il [collaudo d'uso](COLLAUDO_SKILL.md) valuta instradamento ed effetti delle risposte reali; i controlli documentali da soli non certificano il comportamento di tutte le AI.

## Raccordo del ciclo di sviluppo v3

Consulta la [mappa delle fasi e dei metodi](../knowledge/03_architettura_e_metodologie/ciclo_sviluppo_e_selezione_strumenti_astralis.md) per distinguere creazione, analisi, validazione, revisione e prove. Revisione corrente del catalogo: 1.3.0; il framework resta 3.0.21.
