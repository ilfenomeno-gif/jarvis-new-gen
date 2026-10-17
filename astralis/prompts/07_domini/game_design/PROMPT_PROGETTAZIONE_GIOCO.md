---
schema: 2
id: "AST-P-GAME-DESIGN"
title: "Progettazione di un gioco accessibile"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "07_domini/game_design"
protocols: [1, 2, 12]
domains: ["giochi"]
mode: "consultiva"
requires: ["lettura_materiali"]
sources: ["prompt-agent-Game-Design-&-Analysis-Engine.md", "prompt-generic-Game Design Analyzer.md"]
selection: {"intents": ["progettare_gioco"], "use_when": ["Definire concept, core loop e minimo giocabile di un gioco accessibile."], "avoid_when": ["Non verifica automaticamente una build esistente e non si applica a domini senza gameplay."], "materials": ["idea_gioco", "pubblico_e_piattaforma_o_da_definire", "vincoli_accessibilita"], "examples": ["Ho un’idea di gioco e voglio definirne il minimo giocabile."], "related": [{"id": "AST-P-COLLAUDO-GAMEPLAY", "when": "Quando esiste una build di test con scenari verificabili."}]}
---

# Progettazione di un gioco accessibile

## Scopo e condizioni d'uso

Trasformare un'idea di gioco in una proposta giocabile, accessibile e proporzionata.

Identificativo: `AST-P-GAME-DESIGN`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 2, 12.
- Domini: giochi.
- Modalità: `consultiva`.
- Capacità richieste: lettura_materiali.
- Input della sessione: Idea: [CONCEPT]. Pubblico e piattaforma: [CONTESTO]. Core loop: [IDEA O DA DEFINIRE]. Vincoli: [TECNICI, ACCESSIBILITÀ, RISORSE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Definire concept, core loop e minimo giocabile di un gioco accessibile.
- Preferisci altro quando: Non verifica automaticamente una build esistente e non si applica a domini senza gameplay.
- Materiali minimi: idea_gioco, pubblico_e_piattaforma_o_da_definire, vincoli_accessibilita. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Ho un’idea di gioco e voglio definirne il minimo giocabile.».
- Passo collegato: `AST-P-COLLAUDO-GAMEPLAY` — Quando esiste una build di test con scenari verificabili.

La [procedura condivisa v3](../../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Progettazione di un gioco accessibile (AST-P-GAME-DESIGN)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Trasformare un'idea di gioco in una proposta giocabile, accessibile e proporzionata.

INPUT
Idea: [CONCEPT]. Pubblico e piattaforma: [CONTESTO]. Core loop: [IDEA O DA DEFINIRE]. Vincoli: [TECNICI, ACCESSIBILITÀ, RISORSE].

PERIMETRO OPERATIVO
Progettazione in chat. Non generare un progetto, modificare codice o ribilanciare un gioco esistente senza mandato. La validazione del concept non è un collaudo del gameplay.

PROCEDURA
1. Recupera obiettivo, pubblico, piattaforma e vincoli già disponibili. Chiedi solo ciò che manca per definire un core loop verificabile.
2. Descrivi azioni del giocatore, feedback, progressione, fallimento e recupero. Per un gioco esistente separa comportamento osservato e proposta nuova.
3. Applica la simmetria Astralis: interazione completa da tastiera e screen reader, informazioni equivalenti visive e sonore, senza impoverire la fruizione dei vedenti. Usa audio posizionale solo quando serve e preserva la priorità vocale; applica gli standard di volume pertinenti del progetto.
4. Definisci la versione minima giocabile e distingui requisiti essenziali da idee future. Scegli ECS, OOP o altri modelli soltanto quando motivati dal contesto.
5. Verifica feature creep, comprensibilità, bilanciamento ipotizzato, vincoli di risorse e condizioni limite. Non confondere una formula ragionevole con bilanciamento dimostrato.
6. Produci una roadmap con prototipo, verifiche e collaudo tastiera/NVDA. Indica contratti e criteri di successo pertinenti senza imporre una geometria 3D a un gioco testuale.

RISULTATO ATTESO
Concept sintetico, core loop, requisiti di accessibilità, minimo giocabile, scelta tecnica motivata, roadmap, rischi e criteri di collaudo.

CRITERI DI VERIFICA
Azioni e feedback comprensibili; tastiera prevista per ogni funzione; equivalenza informativa; scope sostenibile; bilanciamento e accessibilità da verificare sul prototipo.

LIMITI E ARRESTO
Non richiedere screenshot come unica prova di accessibilità. Se il concept è ancora ambiguo consegna le decisioni necessarie prima di una specifica definitiva.
```

## Esempio di attivazione

Progetta un gioco testuale basato sulla manipolazione del tempo, fruibile con tastiera e NVDA. Definisci prima il minimo giocabile.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-game-engine per aspetti tecnici pertinenti; game design e implementazione del motore restano distinti.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
