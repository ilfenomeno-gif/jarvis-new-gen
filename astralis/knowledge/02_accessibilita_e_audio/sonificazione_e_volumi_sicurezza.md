# Sonificazione, Audio 3D Posizionale e Volumi di Sicurezza
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento definisce gli standard per la progettazione del paesaggio sonoro (soundscape), audio posizionale 3D e protezione acustica per utenti non vedenti.

---

## 🎚️ 1. VOLUMI DI SICUREZZA CONGELATI

1. **Soglia Massima Assoluta (0.7f - 0.8f)**:
   - Tutti gli effetti sonori (SFX), la musica ambientale e i suoni di interfaccia devono avere un master volume non superiore al range compreso tra `0.70` (70%) e `0.80` (80%).
   - Questa soglia garantisce un margine di sicurezza (headroom acustico) affinché la sintesi vocale di NVDA rimanga **sempre perfettamente nitida, udibile e comprensibile** in qualsiasi circostanza.

2. **Duck Audio Dinamico**:
   - Quando viene emesso un messaggio vocale critico o un log prioritario di gioco/sistema, il volume degli SFX e della musica deve abbassarsi automaticamente (ducking) di almeno il 40-50% per la durata del parlato.

---

## 🎧 2. SOUND DESIGN & AUDIO POSIZIONALE 3D

1. **Sonificazione degli Eventi**:
   - Ogni azione (apertura menu, cambio selezione, conferma, errore, collisione) deve avere un feedback audio univoco e differenziato per timbro o altezza (pitch).
   - Suoni brevi, puliti, con attacco rapido (punchy) e senza code riverberanti eccessive che possano mascherare la voce.

2. **Audio Spaziale & Panning Stereofonico**:
   - Utilizzo di librerie audio 3D (OpenAL, FMOD, XAudio2, Pygame sound) per posizionare le sorgenti sonore nello spazio stereo/surround.
   - Panning orizzontale chiaro (Sinistra/Centro/Destra) e attenuazione con la distanza per guidare il movimento e l'orientamento dell'utente.

---

## 🛡️ 3. DINAMICA ACUSTICA E FLOOR MINIMO PER SORGENTI OCCLUSE

1. **Protezione della Rilevabilità (Floor Minimo 1% / 0.01f)**:
   - Quando si applicano filtri di occlusione o attenuazioni cumulative da ostacoli/distanza, il volume scalato non deve mai essere azzerato completamente.
   - Mantenere sempre una soglia minima garantita dell'**$1\%$ (`0.01f`)**, sufficiente a trasmettere la presenza del target alle cuffie ad alta dinamica senza creare 'buchi' informativi.
2. **Prevenzione del Sovraccarico Acustico (Headroom Vocale)**:
   - Suoni occlusi da pareti o ostacoli devono scendere sotto il range di $0.20\text{f} - 0.40\text{f}$ per liberare spazio acustico per la sintesi vocale e i segnali prioritari di allerta.

---

## 👣 4. PROPRIOCEZIONE ACUSTICA & GUADAGNO MIRATO DEL GIOCATORE LOCALE

1. **Il Ruolo Propriocezione dei Passi**:
   - Per un utente non vedente, il suono dei passi del proprio personaggio è l'equivalente della sensazione cinestetica e tattile sotto la suola delle scarpe.
2. **Isolamento della Sorgente Sonora**:
   - L'amplificazione dei passi non deve mai essere applicata all'intero bus audio o a tutti i personaggi, ma circoscritta chirurgicamente alla sola entità controllata dall'utente.
   - Questo previene l'effetto cacofonico e preserva l'headroom acustico per la sintesi vocale e i segnali di allarme.



---

## ⚡ 5. ALLARMI DI EMERGENZA SALVAVITA & PENETRAZIONE VOCALE (TRANSIENTI ACUTI)

1. **Il Principio dei Transienti Metallici Acuti**:
   - I suoni di allerta di emergenza e pre-freno imminente (es. ciglio di un baratro, trappola letale, pericolo mortale istantaneo) non devono mai utilizzare toni sordi, morbidi o a bassa frequenza. Tali toni verrebbero facilmente coperti e mascherati dalla sintesi vocale TTS / NVDA in riproduzione contemporanea.
   - È fatto obbligo di impiegare campioni sonori dotati di un attacco istantaneo (transiente d'impatto ad altissima energia) e spettro armonico acuto metallico (es. risonanza d'incudine su ferro). Il picco frequenziale buca istantaneamente il parlato senza richiedere volumi pericolosi per l'apparato uditivo ($0.7\text{f} - 0.8\text{f}$).

2. **Indipendenza del Canale Audio (Bus Personale vs Ambiente)**:
   - I segnali sonori critici per l'incolumità personale del giocatore non devono mai essere emessi sui bus audio ambientali o degli elementi del mondo (es. `BLOCKS` o `WORLD`), dove le impostazioni utente o i filtri di riverbero possono attenuarli.
   - Devono essere sempre instradati sul canale audio diretto del giocatore (`PLAYERS`, `UI` o `SYSTEM`), garantendo immunità assoluta da filtri di occlusione o cursori di volume dell'ambiente.

---

## 🔔 6. UNIVOCITÀ TIMBRICA, TASSONOMIA DEI SENSORI E DISACCOPPIAMENTO SPAZIALE

1. **Univocità Timbrica Assoluta per Segnali a Diversa Funzione Operativa**:
   - Due eventi sonori a valenza differente (es. radar orografico per dislivelli/voragini del terreno vs scanner per oggetti/waypoint) non devono mai condividere la stessa famiglia di timbri, nemmeno modulando il pitch.
   - La variazione di frequenza dello stesso timbro induce affaticamento cognitivo ed errori interpretativi per l'orecchio del non vedente. È obbligatorio assegnare timbri fisici distinti (es. timbro tellurico/cavernoso tipo *Didgeridoo* per baratri profondi vs campana metallica per punti di interesse).

2. **Tassonomia dei Sensori: Sentinella Attiva di Pericolo vs Radar Passivo di Orientamento**:
   - *Sentinella Attiva*: Raggio d'azione ravvicinato ($0-6\text{ m}$), alta priorità d'allerta, salvavita (es. allarme per minaccia ostile alle spalle, ciglio baratro).
   - *Radar Passivo di Orientamento*: Raggio d'azione medio-ampio ($7-24\text{ m}$), frequenza ritmata periodica, consapevolezza ambientale.
   - *Regola di Coesistenza e Disaccoppiamento Comandi*: L'utente deve poter silenziare/riattivare il ticchettio del radar periodico per eliminare il chiacchiericcio di fondo durante il lavoro o la deambulazione sicura, **senza mai disattivare la sentinella attiva di difesa**. I comandi di toggle devono essere indipendenti e dedicati.

3. **Disaccoppiamento tra Silenziamento Acustico e Scansione Spaziale**:
   - Silenziare l'emissione acustica di una categoria (oggetti, porte, minerali, fluidi) non deve mai interrompere né alterare il ciclo di scansione spaziale e aggiornamento logico dell'ambiente.
   - Il modello del mondo continua ad essere tracciato a pieno regime per il mirino, la lettura coordinate e la sintesi vocale; solo il trigger del playback sonoro viene intercettato e soppresso.

---

## 🎹 7. SINTESI PROCEDURALE IN MEMORIA DI EARCONS (ZERO ASSET BINARI ESTERNI)

1. **Il Principio della Sintesi Procedurale di Interfaccia**:
   - Nei simulatori e nei giochi accessibili, i feedback sonori di navigazione (Earcons / Audio Cues) possono essere generati interamente a runtime in memoria tramite algoritmi di sintesi (forme d'onda sinusoidali, triangolari, d'organo o accordi fisici con inviluppo ADSR), convertiti direttamente in array di byte PCM 16-bit mono a frequenza di campionamento sicura (22.050 Hz).
2. **Vantaggi Architetturali**:
   - **Zero Dipendenze da File Binari**: Elimina il rischio di crash a runtime per file `.wav` o `.ogg` non trovati, corrotti o non inclusi nel pacchetto di rilascio;
   - **Zero Bloat per i Repository Git**: Mantiene i commit leggeri e puramente testuali, evitando di memorizzare mega-file binari sonori nel version control;
   - **Determinismo Headless a 0 ms**: Nei test automatizzati e nelle CI/CD headless, il sistema può istanziare, generare e convalidare i flussi sonori istantaneamente senza dipendere da hardware audio fisico o driver sonori attivi.
3. **Caching & Vincoli di Sicurezza**:
   - Gli stream generati in memoria devono essere memorizzati in una cache dizionario/mappa interna al primo utilizzo per azzerare il carico computazionale della CPU;
   - Ogni campione generato deve rispettare rigidamente la soglia massima del **$0.75\text{f}$ ($-2.5\text{ dB}$)** ed essere collegato a un bus o controller dotato di ducking automatico (abbattimento al $40\%$ durante la sintesi vocale di sistema).
4. **Protezione dei Mixer Dummy nei Test Headless (Prevenzione Leak ObjectDB)**:
   - Nei motori e framework eseguiti in modalità `--headless` (dove il driver audio è un dummy server che non fa avanzare il mixer dei campioni), la chiamata effettiva di riproduzione (`play()`) alloca risorse C++ interne che non giungono mai a termine e causano memory leak (`ObjectDB instances leaked at exit`).
   - È regola universale proteggere l'invocazione di `play()` verificando l'ambiente (`if not is_headless`), consentendo la completa generazione dello stream in memoria, la registrazione in cache e il calcolo dei volumi/ducking a 0 ms senza allocazioni orfane. All'arresto dei suoni e al termine dei test, azzerare lo stream del player (`player.stream = null`) e invocare il silenziamento d'emergenza.

---

## 🔀 8. DISACCOPPIAMENTO HARDWARE DEI CANALI DI RIPRODUZIONE (ISOLAMENTO AUDIO GIOCO VS SINTESI VOCALE)

1. **Il Principio dell'Isolamento Hardware dei Canali Uditivi**:
   - Nei videogiochi complessi o mondi virtuali 3D ad alto carico dinamico, il paesaggio sonoro (esplosioni, effetti meteorologici, musiche di combattimento, suoni ambientali) tende a saturare l'intero spettro acustico udibile;
   - Se l'audio di gioco e la sintesi vocale dello screen reader (NVDA, JAWS, VoiceOver, Orca) convergono sulla medesima periferica fisica (singola cuffia o cassa), si verifica un fenomeno di **mascheramento acustico distruttivo** che rende incomprensibile la voce di interfaccia vitale, costringendo l'utente ad alzare la sintesi a volumi dannosi per l'apparato uditivo;
   - Principio universale: l'ecosistema o mod accessibile deve consentire il reindirizzamento hardware indipendente del flusso sonoro del gioco verso una periferica specifica (es. altoparlanti da tavolo o headset da gioco), preservando un'uscita dedicata (es. auricolare secondario o cuffie a conduzione ossea) per la sintesi vocale dello screen reader.

2. **Invariante di Stabilità Runtime e Fallback Deterministico**:
   - Nelle API audio a grafo e mastering voice (DirectX XAudio2, WASAPI, CoreAudio, ALSA), l'assegnazione della periferica hardware fisica deve avvenire all'inizializzazione del motore o della sessione audio;
   - È vietato tentare la distruzione forzata ("teardown a caldo") dei nodi radice o delle mastering voice mentre sono in corso stream sonori attivi, poiché tale operazione genera access violation o crash irreversibili;
   - In caso di periferica disconnessa, spenta o rimossa, il sistema deve garantire un fallback deterministico e trasparente sulla periferica predefinita di sistema (indice `0`), prevenendo qualsiasi blocco della riproduzione o crash dell'applicazione.


