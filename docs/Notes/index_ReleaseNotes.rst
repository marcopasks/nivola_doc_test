.. _news:

**Release Notes**
===================================

.. _release-2.3.0:

Service Portal 2.3.0 (2021-04-09)
---------------------------------

**New**

*   Gestione completa delle snapshot VM. La funzionalità comprende:

    *   `[NSP-188] <https://jira.csi.it/browse/NSP-188>`_ - Creazione nuova snapshot per VM
	
    *   `[NSP-189] <https://jira.csi.it/browse/NSP-189>`_ - Revert snapshot su VM
	
    *   `[NSP-359] <https://jira.csi.it/browse/NSP-359>`_ - Cancellazione snapshot VM

*   `[NSP-113] <https://jira.csi.it/browse/NSP-113>`_ - Compute Service - Visualizzazione lista Volumi associati all'Account
    
*   `[NSP-168] <https://jira.csi.it/browse/NSP-168>`_ - Visualizzazione e gestione Notizie con layout grafico

*   `[NSP-466] <https://jira.csi.it/browse/NSP-466>`_ - L'utente di BackOffice può visualizzare le quote relative ai singoli account

*   `[NSP-516] <https://jira.csi.it/browse/NSP-516>`_ - Inserita la nuova sezione Documentazione - SLA 

*   `[NSP-477] <https://jira.csi.it/browse/NSP-477>`_ - Primo prototipo versione Inglese del Service Portal 
    
**Changed**

*   `[NSP-465] <https://jira.csi.it/browse/NSP-113>`_ - Modificata la visualizzazione delle Quote di un Account distinguendola per singolo Servizio (Compute, DBaas, Staas)

*   `[NSP-493] <https://jira.csi.it/browse/NSP-493>`_ - Nuova modalità di visualizzazione del menù laterale di navigazione

*   `[NSP-530] <https://jira.csi.it/browse/NSP-530>`_ - Refactoring SP per adeguamento e miglioramento gestione "ruolo Utente"

*   `[NSP-477] <https://jira.csi.it/browse/NSP-530>`_ - Miglioramento presentazione dati report PDF di dettaglio

**Fixed**    
    
*   `[NSP-132] <https://jira.csi.it/browse/NSP-132>`_ - Risolto problema funzionalità di modifica/cambio Security Group

*   `[NSP-553] <https://jira.csi.it/browse/NSP-553>`_ - Risolto problema di inserimento Notizie contenenti TAG HTML

*   `[NSP-551] <https://jira.csi.it/browse/NSP-551>`_ - Le azioni di cambio Flavour VM vengono ora inserite nella cronologia attività account

*   `[NSP-390] <https://jira.csi.it/browse/NSP-390>`_ - `[NSP-563] <https://jira.csi.it/browse/NSP-563>`_ - `[NSP-442] <https://jira.csi.it/browse/NSP-442>`_ - `[NSP-572] <https://jira.csi.it/browse/NSP-572>`_ - `[NSP-557] <https://jira.csi.it/browse/NSP-557>`_ - `[NSP-555] <https://jira.csi.it/browse/NSP-555>`_ - `[NSP-330] <https://jira.csi.it/browse/NSP-536>`_ - `[NSP-536] <https://jira.csi.it/browse/NSP-515>`_ 



===================================

.. _release-2.2.0:

Service Portal 2.2.0 (2021-02-17)
---------------------------------

**New**

*   `[NSP-120] <https://jira.csi.it/browse/NSP-120>`_  - L'utente Master di account può visualizzare le quote del proprio Account
    
*   `[NSP-132] <https://jira.csi.it/browse/NSP-132>`_ - Modifica/Cambio Security Group VM per Master di Account.

*   `[NSP-140] <https://jira.csi.it/browse/NSP-140>`_ - Nuova funzionalità di Eliminazione/Rimozione STAAS 

*   `[NSP-187] <https://jira.csi.it/browse/NSP-187>`_ - Visualizzazione lista Snapshot Virtual Machine

*   `[NSP-207] <https://jira.csi.it/browse/NSP-207>`_ - integrazione consumi e calcolo costi SQLServer

*   `[NSP-319] <https://jira.csi.it/browse/NSP-319>`_ - Elenco Dbaas, visualizzazione e possibilità di effettuare ricerche per tags

*   `[NSP-300] <https://jira.csi.it/browse/NSP-300>`_ - Lista VM - aggiunta colonna Securiy Group

*   Inserimento e adeguamento listino 2021
    

    
**Changed**

*  `[NSP-237] <https://jira.csi.it/browse/NSP-237>`_ - riorganizzazione report pdf e raggruppamenti Costi e Consumi

*  `[NSP-180] <https://jira.csi.it/browse/NSP-180>`_ - adeguamento presentazione costi e consumi su Service Portal

*  `[NSP-288] <https://jira.csi.it/browse/NSP-288>`_ - creazione SG - Ripristino funzionalità

*  `[NSP-412] <https://jira.csi.it/browse/NSP-412>`_ - Adeguamento strutture dati e gestione listino 2021

*  `[NSP-274] <https://jira.csi.it/browse/NSP-274>`_ - Miglioramento interfaccia presentazione rendiconti costi e consumi


**Fixed**    
    
*   `[NSP-186] <https://jira.csi.it/browse/NSP-186>`_ - Risolto problema bloccante creazione regole Security Group

*   `[NSP-208] <https://jira.csi.it/browse/NSP-208>`_ - Risolto bug campo "Descrizione" in creazione regole SG

*   `[NSP-183] <https://jira.csi.it/browse/NSP-183>`_ - Lista bud presentazione SecurityGroup maggiore di 10

*   `[NSP-225] <https://jira.csi.it/browse/NSP-225>`_ - Bug paginazione visualizzazione servizi account

*   `[NSP-153] <https://jira.csi.it/browse/NSP-153>`_ - `[NSP-184] <https://jira.csi.it/browse/NSP-184>`_ - `[NSP-186] <https://jira.csi.it/browse/NSP-186>`_ - `[NSP-249] <https://jira.csi.it/browse/NSP-249>`_ - `[NSP-266] <https://jira.csi.it/browse/NSP-266>`_ - `[NSP-321] <https://jira.csi.it/browse/NSP-321>`_ - `[NSP-330] <https://jira.csi.it/browse/NSP-330>`_ - `[NSP-319] <https://jira.csi.it/browse/NSP-319>`_ - `[NSP-342] <https://jira.csi.it/browse/NSP-342>`_



.. _release-2.1.0:

Service Portal 2.1.0 (2020-10-14)
---------------------------------

**New**

*   Aggiunta la gestione TAG anche per gli oggetti di tipo STaaS.
    
*   Nelll'elenco delle VM per Account viene visualizzata anche la colonna Tag. E' quindi possibile 
    effettuare la ricerca anche su questo campo Tag.

*   L'utente di Backoffice può visualizzare i Security Group e i VPC degli Account. 

*   E' ora possibile visualizzare i Costi e Consumi anche relativi ad un'Organizzazione

*   L'utente Master/Viewer di account può consultare l'elenco dei servizi di gestione attivati sulle
    proprie risorse
    

    
**Changed**

*   Migliorati i report pdf/csv relativi ai Costi e Consumi mensili.

*   Il report pdf di dettaglio mensile Costi è ora accedibile e scaricabile direttamente
    dalla voce di menu "Costi e Consumi"



**Fixed**    
    
*   Risolto bug #1118. La naming convention dei dbaas non prevede caratteri minuscoli.

*   Migliorata la fruibilità della funzione di add rule per i Security Group (#1113)

*   I Tag relativi agli oggetti VM, DBaaS, STaaS possono contenere fino a 64 caratteri (#1083) 

*   Risolti bug #1137, #1117, #1114, #1113, #1058, #594



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
    
*   Integrazione con il sistema di ticketing  Remedy per le richieste di supporto sugli oggetti DBaaS 
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

*   Issue #1071, #1072 relative alla creazione vm con immagini Microsoft.


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


