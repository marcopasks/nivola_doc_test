.. _news:

**Release Notes**
===================================

.. _release-2.0.0:

Service Portal 2.0.0 (2020-07-29)
---------------------------------

**New**

*   Upgrade tecnologico in modo da sfruttare le potenzialità del deploy della CMP 
    su un cluster Kubernates. Maggiore affidabilità e scalabilità del sistema.
    
*   In fase di creazione di virtual machine, DBaaS e STaaS è ora possibile avere la previsione del costo
    mensile delle risorse che si intendono allocare.

*   Completa gestione dei TAG sugli oggetti VM e DBaaS.

*   Nuova funzioanlità di autoregistrazione sul SP per gli utenti Csi. 

*   Revisione della funzionalità "Costi e Consumi". E' ora disponibile per tutti i profili con una
    migliore fruibilità dei dati. Aggiunta la possiblità di avere i costi aggregati per Divisione
    e Organizzazione.
    
*  Integrazione con il sistema di ticketing  Remedy per le richieste di supporto sugli oggetti DBaaS 
   effettuate tramite Service Portal.

    
**Changed**

*   Migliorata la navigazione all'interno delle procedure guidate di creazione servizi.

*   Aggiornata la naming convention per i servizi DBaaS.

*   Aggiunti nuovi tagli per il dimensionamento dei Volumi e dei dischi.

*   Migliorato il sistema di gestione Errori.

*   Evoluzione delle procedure di calcolo giornaliero dei costi con generazione di report pdf e csv

    

**Fixed**    
    
*   Risolti bug #972 #975 #976 relativo alla corretta presentazione dei servizi per i profili
    Master di Division e Organization.

*   Risolto il problema  #936  #937 per la visualizzazione liste strutture organizzative.

*  Issue #1071, #1072 relative alla creazione vm con immagini Microsoft.


.. _release-1.9.0:

Service Portal 1.9.0 (2020-05-06)
---------------------------------

**New**

*   E' disponibile una nuova funzionalità per l'utente di Backoffice per visualizzare la
    cronologia delle operazioni effettuate all'interno di ogni Account. 
    
*   L'utente "Master di Account" adesso può visualizzare lo storico delle operazioni effettuate 
    all'interno del proprio account da parte di quasiasi utente.

*   E' disponibile la nuova voce di menu "Log Management" che permette di accedere al servizio
    di gestione log della piattaforma. 
    

    
**Changed**

*   Modificata la naming convention per i servizi DBaaS.

*   Aggiunto un attributo ad ogni account con cui è possibile specificare la data di inizio
    rendicontazione.

*   Adeguamento grafico nella presentazione dei pannelli costi e consumi.

*   Nel pannello di gestione di un DBaaS è  ora possibile visualizzare eventuali dischi aggiuntivi.

    

**Fixed**    
    
*   Risolto bug #907 relativo alla corretta presentazione dei dati nella dashboard "Servizi attivi Account".

*   Risolto il problema  #929 della visualizzazione dell'elenco utenti per il MAster di Divisione.

*   I dati presentati nella dashboard "Storage" sono stati corretti #906

.. _release-1.8.0:

Service Portal 1.8.0 (2020-04-10)
---------------------------------

**New**

*   Rilasciato nuovo ruolo utente "Viewer di Account":  da oggi potranno essere accreditati
    utenti con il ruolo di Viewer di Account. Per i dettagli operativi del ruolo si rimanda 
    alla sezione :ref:`Utenti, Ruoli ed Account <utenti-ruoli>`

*   l'utente Master di Divisione ha a disposizione una nuova funzionalità in modo da poter
    accreditare e registare utenti all'interno della propria struttura organizzativa.
    
*   l'utente con ruolo Master di Account ha a disposizione una nuova funzionalità con cui
    può accreditare e revocare accreditamenti all'interno della propria struttura organizzativa.
 
*   l'utente con ruolo di BackOffice ha ha disposizione la ossibilità di visualizzare tutti  i
    Servizi istanziati all'intefno di ogni Account.
    
**Changed**

*   La form di richiesta utenze su DBAAS è stata aggiornata con la possibilità di richiedere utenze Amministrative

*   Aggiornata la procedura guidata per la creazione di VM con s.o. Windows in modo da accettare password sicure

*   La grafica e il contenuto del pannello Costi e Consumi di un Account sono stati rivisti e migliorati.

*   Nel pannello di gestione di una Vm è  ora possibile visualizzare eventuali dischi aggiuntivi.

    

**Fixed**    
    
*   Risolto bug #803 sulla creazione di Vm con immagine Oracle Linux.

*   Adeguati i tagli delle dimensioni degli Share e dei dischi aggiuntivi di VM e DBAAS.

*   Bux fixing su alcune informazioni contenute nella home page dell'uente Master di Account (#779)


