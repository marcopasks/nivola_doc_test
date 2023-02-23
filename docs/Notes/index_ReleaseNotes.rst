.. _news:

**Release Notes**
===================================

.. _release-3.2.0:

Service Portal 3.2.0 (2023-02-23)
---------------------------------

Le principali novità introdotte:

- possibilità di monitorare le Virtual Machine grazie all'utilizo di uno specifico strumento software per il monitoraggio di risorse IT

- possibilità di accedere e verificare i log di sistema delle Virtual Machine sulla piattaforma Grafana attraverso il motore di ricerca Elasticsearch

- possibilità di verificare lo stato e il contenuto dei backup


**New**

*   `[NSP-1878] <https://jira.csi.it/browse/NSP-1878>`_ - Form per richiesta servizio remotizzazione TSplus
*   `[NSP-1907] <https://jira.csi.it/browse/NSP-1907>`_ - Visualizzare Quote Servizio logging
*   `[NSP-1914] <https://jira.csi.it/browse/NSP-1914>`_ - CDU 05 (FE) - dettagliare la sezione di Log Management
*   `[NSP-1918] <https://jira.csi.it/browse/NSP-1918>`_ - Monitoring: elenco istanze monitoraggio
*   `[NSP-1922] <https://jira.csi.it/browse/NSP-1922>`_ - Monitoring - Attivazione su VM (Linux)
*   `[NSP-1923] <https://jira.csi.it/browse/NSP-1923>`_ - Backend attivazione monitoraggio su VM
*   `[NSP-1930] <https://jira.csi.it/browse/NSP-1930>`_ - Elenco folders Monitoring Account
*   `[NSP-1933] <https://jira.csi.it/browse/NSP-1933>`_ - Sincronizza utenti Account con Utenti accreditati sul Folder Monitoring corrispondente
*   `[NSP-1940] <https://jira.csi.it/browse/NSP-1940>`_ - Il B.O. visualizza la Lista delle VM con Logging attivo
*   `[NSP-1942] <https://jira.csi.it/browse/NSP-1942>`_ - Il Master/Viewer visualizza la Lista delle VM con Logging attivo
*   `[NSP-1943] <https://jira.csi.it/browse/NSP-1943>`_ - Visualizzazione quote Logging per Master/Viewer e Backoffice
*   `[NSP-1945] <https://jira.csi.it/browse/NSP-1945>`_ - Lista Spaces Elastic per Account
*   `[NSP-1947] <https://jira.csi.it/browse/NSP-1947>`_ - Sincronizzazione utenti Account con Sistema Logging
*   `[NSP-1949] <https://jira.csi.it/browse/NSP-1949>`_ - Attivazione Logging per una VM
*   `[NSP-1952] <https://jira.csi.it/browse/NSP-1952>`_ - Disattivazione Logging da una VM
*   `[NSP-1957] <https://jira.csi.it/browse/NSP-1957>`_ - Disattivazione Monitoring da VM (destrumentazione)
*   `[NSP-1960] <https://jira.csi.it/browse/NSP-1960>`_ - Connessione dashboard (Grafana) per il folder selezionato
*   `[NSP-1961] <https://jira.csi.it/browse/NSP-1961>`_ - Sincronizzazione utenti Account con utenti Grafana (Monitoraggio)
*   `[NSP-2070] <https://jira.csi.it/browse/NSP-2070>`_ - Ripristina visualizzazione Backup Openstack (Trilio)

**Changed**

*   `[NSP-1998] <https://jira.csi.it/browse/NSP-1998>`_ - Volumi su SP : Gestione della tecnologia
*   `[NSP-1454] <https://jira.csi.it/browse/NSP-1454>`_ - Ruolo Amm. Backoffice : gestire data di cancellazione
*   `[NSP-1691] <https://jira.csi.it/browse/NSP-1691>`_ - Frontend: inibire l'apertura di di tab sull'applicazione.
*   `[NSP-1981] <https://jira.csi.it/browse/NSP-1981>`_ - Renderizzazine dati Dettaglio VM
*   `[NSP-1994] <https://jira.csi.it/browse/NSP-1994>`_ - Segnalazione anomalia report costi per WBS
*   `[NSP-2033] <https://jira.csi.it/browse/NSP-2033>`_ - Box "Costi" Homepage primo giorno del mese
*   `[NSP-1874] <https://jira.csi.it/browse/NSP-1874>`_ - Verifica su criteri determinazione tecnologia DBAAS
*   `[NSP-1929] <https://jira.csi.it/browse/NSP-1929>`_ - eliminare voce di menu AppEngine dal left menu per il ruolo Account admin
*   `[NSP-1983] <https://jira.csi.it/browse/NSP-1983>`_ - STAGE: modifica messaggio FE logging service se servizio non attivo
*   `[NSP-2034] <https://jira.csi.it/browse/NSP-2034>`_ - DBAAS : Aggiungere il termine "stimati" per il dato spazio disco
*   `[NSP-2039] <https://jira.csi.it/browse/NSP-2039>`_ - elenco spaces (in Strumenti -> Log management)

**Fixed**    

*   `[NSP-2051] <https://jira.csi.it/browse/NSP-2051>`_ - rivedere messaggio e gestione creazione VM in caso di "Quotas compute.cores have been exceeded"
*   `[NSP-1984] <https://jira.csi.it/browse/NSP-1984>`_ - STAGE: errore Richiesta TSPLus
*   `[NSP-1985] <https://jira.csi.it/browse/NSP-1985>`_ - STAGE: schermata bianca in Quote servizi -> Monitoraggio
*   `[NSP-1986] <https://jira.csi.it/browse/NSP-1986>`_ - STAGE: correzione titolo in Strumenti -> VM
*   `[NSP-1987] <https://jira.csi.it/browse/NSP-1987>`_ - STAGE: in quote servizi, eliminare messaggio errato durante attesa utente
*   `[NSP-1988] <https://jira.csi.it/browse/NSP-1988>`_ - STAGE: correzione label "Nessuna dato Ã¨ stato trovato per l'Account." in quote servizi




.. _release-3.1.0:

Service Portal 3.1.0 (2022-12-20)
---------------------------------

**Fixed**    
    
*   `[NSP-1871] <https://jira.csi.it/browse/NSP-1871>`_ - Errore "Servizio outer API non disponibile" tentando di aprire una segnalazione su Troubleticketing

*   `[NSP-1886] <https://jira.csi.it/browse/NSP-1886>`_ - Errore in prospetto costi stimati

*   `[NSP-1674] <https://jira.csi.it/browse/NSP-1674>`_ - Ticket chiuso : inibire modifica dell'assegnatario

**Changed**

*   `[NSP-1813] <https://jira.csi.it/browse/NSP-1813>`_ - Network Vulnerability Assesment

*   `[NSP-1861] <https://jira.csi.it/browse/NSP-1861>`_ - Modifica Account (backoffic) : Reintegrare data inizio valorizzazione consumi

*   `[NSP-1828] <https://jira.csi.it/browse/NSP-1828>`_ - Richiesta per Sistemi di cifratura (DBAAS)





.. _release-3.0.6:

Service Portal 3.0.6 (2022-12-10)
---------------------------------

**Fixed**    
    
*   `[NSP-1867] <https://jira.csi.it/browse/NSP-1867>`_ - Problema di Failover su cluster Galera MariaDB

*   `[NSP-1869] <https://jira.csi.it/browse/NSP-1869>`_ - problema paginazione lista VM




.. _release-3.0.5:

Service Portal 3.0.5 (2022-12-06)
---------------------------------

**Fixed**    
    
*   `[NSP-1864] <https://jira.csi.it/browse/NSP-1864>`_ - Bug di regressione - Utenti non riescono ad aprire ticket

**Changed**

*   `[NSP-1374] <https://jira.csi.it/browse/NSP-1374>`_ - Sospendere rendicontazione account

*   `[NSP-1837] <https://jira.csi.it/browse/NSP-1837>`_ - Revisione report CSV costi/consumi (ordine colonne come Listino)

*   `[NSP-1838] <https://jira.csi.it/browse/NSP-1838>`_ - Report (CSV) Accounts con Referente e dati anagrafici




.. _release-3.0.4:

Service Portal 3.0.4 (2022-12-05)
---------------------------------

**Changed**

*   `[NSP-1692] <https://jira.csi.it/browse/NSP-1692>`_ - Modifica Anagrafica Account - Gestione WBS

*   `[NSP-1850] <https://jira.csi.it/browse/NSP-1850>`_ - Algoritmo assegnazione nomi a DBAAS SQLServer

*   `[NSP-1769] <https://jira.csi.it/browse/NSP-1769>`_ - Adeguamento backend per miglioramento performance "Servizi Attivi"

*   `[NSP-1783] <https://jira.csi.it/browse/NSP-1783>`_ - Backoffice - Visualizza Dettaglio Account : Visualizzare ripartizione WBS

*   `[NSP-1789] <https://jira.csi.it/browse/NSP-1789>`_ - Offuscare/Inibire funzionalità snapshot sul Service Portal

*   `[NSP-1812] <https://jira.csi.it/browse/NSP-1812>`_ - Modifica utente: il campo cmp username diventa null@domnt.csi.it


**Fixed**    
    
*   `[NSP-1818] <https://jira.csi.it/browse/NSP-1818>`_ - Problemi su Stampa Consumi per Wbs

*   `[NSP-1846] <https://jira.csi.it/browse/NSP-1846>`_ - Inserimento associazione account - Listino : data inizio associazione può essere nel passato!

*   `[NSP-1759] <https://jira.csi.it/browse/NSP-1759>`_ - segnalazione bug su Elenco Division - Account

*   `[NSP-1849] <https://jira.csi.it/browse/NSP-1849>`_ - Messaggio di configurazione ticket da correggere




.. _release-3.0.3:

Service Portal 3.0.3 (2022-11-24)
---------------------------------

**Changed**

*   `[NSP-1806] <https://jira.csi.it/browse/NSP-1806>`_ - Creazione report CSV utenti con ruolo CMP

*   `[NSP-1767] <https://jira.csi.it/browse/NSP-1767>`_ - Censimento (automatico) account sconosciuti al service portal

*   `[NSP-1695] <https://jira.csi.it/browse/NSP-1695>`_ - Modifica Anagrafica Account - Gestione Person_id (integrazione sistema Ticketing)




.. _release-3.0.2:

Service Portal 3.0.2 (2022-11-08)
---------------------------------

**Changed**

*   `[NSP-1760] <https://jira.csi.it/browse/NSP-1760>`_ - Nome della risorsa VM : verifica che sia composto solo da caratteri alfanumerici e '-'


**Fixed**    
    
*   `[NSP-1751] <https://jira.csi.it/browse/NSP-1751>`_ - Verificare errore al caricamento del front.end ($sce)

*   `[NSP-1754] <https://jira.csi.it/browse/NSP-1754>`_ - Logout con SPID non termina la sessione SPID

*   `[NSP-1756] <https://jira.csi.it/browse/NSP-1756>`_ - REMEDY: errore mancata configurazione account

*   `[NSP-1758] <https://jira.csi.it/browse/NSP-1758>`_ - Tabella Elenco VM - frecce di navigazione non abilitate

*   `[NSP-1755] <https://jira.csi.it/browse/NSP-1755>`_ - verifica funzionalità Ricalcolo Costi Account




.. _release-3.0.1:

Service Portal 3.0.1 (2022-11-06)
---------------------------------

**Fixed**    
    
*   `[NSP-1778] <https://jira.csi.it/browse/NSP-1778>`_ - Lista VM vuota (produzione)

*   `[NSP-1746] <https://jira.csi.it/browse/NSP-1746>`_ - da lista VM il tasto "pannello di controllo VM" non funzionante (PRODUZIONE)




.. _release-3.0.0:

Service Portal 3.0.0 (2022-11-04)
---------------------------------

**New**

*   `[NSP-1716] <https://jira.csi.it/browse/NSP-1716>`_ - Modifica Anagrafica Account - Associazione Account con Listino (specifico)

*   `[NSP-1246] <https://jira.csi.it/browse/NSP-1246>`_ - Gestione attributo "Listino Associato all'Account"

*   `[NSP-1609] <https://jira.csi.it/browse/NSP-1609>`_ - Evidenziare/segnalare quando un utente chiede di aprire un ticket su un account non correttamente configurato

*   `[NSP-1686] <https://jira.csi.it/browse/NSP-1686>`_ - Caricamento pannello VM : mettere animazione di attesa

*   `[NSP-1735] <https://jira.csi.it/browse/NSP-1735>`_ - Caricamento pannello DBAAS : mettere animazione di attesa

*   `[NSP-1581] <https://jira.csi.it/browse/NSP-1581>`_ - Dettaglio VM : Elenco Restore Points disponibili per la VM

*   `[NSP-1614] <https://jira.csi.it/browse/NSP-1614>`_ - inserire interfaccia standard frontend per "attesa utente" per "Scarica report csv per servizio vm" e report simili


**Changed**

*   `[NSP-1664] <https://jira.csi.it/browse/NSP-1664>`_ - Crea nuova VM : Composizione FQDN VM Windows : non usare acronimo

*   `[NSP-1631] <https://jira.csi.it/browse/NSP-1631>`_ - Revisione pannello "Edit Account" - Progettazione

*   `[NSP-1562] <https://jira.csi.it/browse/NSP-1562>`_ - non più presente stato provvisorio"BUILDING" dal portale in caso di riavvi e/o operazioni su una VM (PROD e STAGE)


**Fixed**    
    
*   `[NSP-1679] <https://jira.csi.it/browse/NSP-1679>`_ - Conteggio risorse nella pagina di Dettaglio su Portale tutti valori a 0

*   `[NSP-1447] <https://jira.csi.it/browse/NSP-1447>`_ - Visualizzazione regole SG : Usare il JSON servizi anche per visualizzare la regola

*   `[NSP-1551] <https://jira.csi.it/browse/NSP-1551>`_ - Costi account non rendicontati : Correzione date

*   `[NSP-1571] <https://jira.csi.it/browse/NSP-1571>`_ - (Amm. Backoffice) Dopo Edit Account se clicco su Accounts limita la ricerca alla Divisione dell'ultimo Account

*   `[NSP-1613] <https://jira.csi.it/browse/NSP-1613>`_ - errore nel ricalcolo costi account specifico

*   `[NSP-1563] <https://jira.csi.it/browse/NSP-1563>`_ - correzione label in caso di detach di un volume

*   `[NSP-1566] <https://jira.csi.it/browse/NSP-1566>`_ - report Amministrazione -> Report -> Report / Tipo di report "Per WBS"




.. _release-2.8.1:

Service Portal 2.8.1 (2022-09-12)
---------------------------------

**New**

*   `[NSP-1537] <https://jira.csi.it/browse/NSP-1537>`_ - Adeguamento evolutivo procedura calcolo costi

*   `[NSP-628] <https://jira.csi.it/browse/NSP-628>`_ - Adeguamento attributi Accounts (billing)

*   `[NSP-1246] <https://jira.csi.it/browse/NSP-1246>`_ - Gestione attributo "Listino Associato all'Account"

*   `[NSP-846] <https://jira.csi.it/browse/NSP-846>`_ - Gestione attributo "Listino Associato all'Account"

*   `[NSP-1250] <https://jira.csi.it/browse/NSP-1250>`_ - CDU GESTIONE WBS – ACCOUNT




.. _release-2.8.0:

Service Portal 2.8.0 (2022-07-30)
---------------------------------

**New**

*   `[NSP-598] <https://jira.csi.it/browse/NSP-598>`_ - Elenco Jobs di Backup delle VM per gli account abilitati

*   `[NSP-1511] <https://jira.csi.it/browse/NSP-1511>`_ - Inserimento nuova associazione WBS - Account

*   `[NSP-1542 - NSP-1475] <https://jira.csi.it/browse/NSP-1542 - https://jira.csi.it/browse/NSP-1475>`_ - Memo orari presa in carico / Pop-up disclaimer all'apertura di un nuovo ticket con riferimento numero telefonico per richieste urgenti

*   `[NSP-1485] <https://jira.csi.it/browse/NSP-1485>`_ - Avviso visivo utente quando l'operazione richiede di attendere


**Changed**

*   `[NSP-1541] <https://jira.csi.it/browse/NSP-1541>`_ - Aggiunta flag "Accedi Sistema Ticketing" su Autoregistrazione

*   `[NSP-1517] <https://jira.csi.it/browse/NSP-1517>`_ - Inserita in mail apertura ticket le informazioni "oggetto" e "testo"


**Fixed**    
    
*   `[NSP-1507] <https://jira.csi.it/browse/NSP-1507>`_ - Salvataggio allegati nelle bozze

*   `[NSP-1519] <https://jira.csi.it/browse/NSP-1519>`_ - Revoca Associazione WBS

*   `[NSP-1500] <https://jira.csi.it/browse/NSP-1500>`_ - DBAAS visualizzaione informazioni "Subnet", "security Security Group" e "IP address



.. _release-2.7.0:

Service Portal 2.7.0 (2022-07-04)
---------------------------------

**New**


*   `[NSP-1249] <https://jira.csi.it/browse/NSP-1249>`_ - Gestione attributo WBS accunt per Operatore di Backoffice
	
*   `[NSP-1448] <https://jira.csi.it/browse/NSP-1448>`_ - Evolutive integrazione sistema di troubleticketing - E' ora possibile visualizzare la priorità del ticket e l'assegnatario


**Changed**

*   `[NSP-1422] <https://jira.csi.it/browse/NSP-1422>`_ - Rimozione TAB gestione utenti per servizio DBAAS

*   `[NSP-1448] <https://jira.csi.it/browse/NSP-1448>`_  - Miglioramento navigazione e layout sistema di troubleticketing

*   `[NSP-1135] <https://jira.csi.it/browse/NSP-1135>`_ - integrazione gestione StaaS di tipologia Netapp


**Fixed**    
    
*   `[NSP-846] <https://jira.csi.it/browse/NSP-846>`_ Download csv Lista Attività / Cronologia



.. _release-2.6.2:

Service Portal 2.6.2 (2022-06-20)
---------------------------------

**Fixed**    
    
*   `[NSP-1440] <https://jira.csi.it/browse/NSP-1440>`_ Verifica tipologia rules inserite in Security Group

*   `[NSP-1094] <https://jira.csi.it/browse/NSP-1094>`_ Risolto bug download report csv risorse DBAAS



.. _release-2.6.1:

Service Portal 2.6.1(2022-06-10)
---------------------------------


**Changed**

*   `[NSP-1451] <https://jira.csi.it/browse/NSP-1451>`_ - eliminazione pulsante creazione snapshot con ruolo "viewer di account"

*   `[NSP-1163] <https://jira.csi.it/browse/NSP-1163>`_ - aggiunto filtro su funzionalità di visualizzazione listino

*   `[NSP-1211] <https://jira.csi.it/browse/NSP-1211>`_ - Lista e dettaglio Volumi. Inserito il dettaglio del Volume Type


**Fixed**    
    

*   `[NSP-1454] <https://jira.csi.it/browse/NSP-1454>`_ - `[NSP-1044] <https://jira.csi.it/browse/NSP-1094>`_ 

*   `[NSP-1158] <https://jira.csi.it/browse/NSP-1158>`_ - Problema con Ruoli CMP Account rimossi (DELETED)

*   `[NSP-1418] <https://jira.csi.it/browse/NSP-1418>`_ - Pagine integrazione troubleTicketing. Manca Link a documentazione

*   `[NSP-1390] <https://jira.csi.it/browse/NSP-1390>`_ 


.. _release-2.6.0:

Service Portal 2.6.0 (2022-06-01)
---------------------------------

**New**


*   `[NSP-1110] <https://jira.csi.it/browse/NSP-1110>`_ - Aggiunta funzionalità "servizi" per l'inserimento regole Security Group
	
*   `[NSP-943] <https://jira.csi.it/browse/NSP-943>`_ - [NSP-1302] <https://jira.csi.it/browse/NSP-1302>`_ - `[NSP-946] <https://jira.csi.it/browse/NSP-946>`_ - `[NSP-945] <https://jira.csi.it/browse/NSP-945>`_ - `[NSP-947] <https://jira.csi.it/browse/NSP-947>`_ - Rilascio versione Beta integrazione strumeno di Trouble Ticketing. Visibilità sridotta a utenti Beta Tester

**Changed**

*   `[NSP-1220] <https://jira.csi.it/browse/NSP-1220>`_ - Revisione etichette scarico Csv

*   `[NSP-545] <https://jira.csi.it/browse/NSP-545>`_ - Abilitazione authoring tramite Token Utente

*   `[NSP-790] <https://jira.csi.it/browse/NSP-790>`_ - Integrazione SP con identity provider stranieri (Beta)


**Fixed**    
    
*   `[NSP-1280] <https://jira.csi.it/browse/NSP-1280>`_ - Adegamento report costi WBS per Amministratore di BackOffice

*   `[NSP-1420] <https://jira.csi.it/browse/NSP-1420>`_ - Aumentato il numero massimo di caratteri sul campo "Note aggiuntive"

*   `[NSP-748] <https://jira.csi.it/browse/NSP-748>`_ - Correzione Bug detach volume disco di root

*   `[NSP-1360] <https://jira.csi.it/browse/NSP-1360>`_ - Lista servizi VM (Amm Backoffice) : Visualizzare tooltip con FQDN VM

*   `[NSP-1287] <https://jira.csi.it/browse/NSP-1287>`_ - `[NSP-1240] <https://jira.csi.it/browse/NSP-1240>`_ - `[NSP-1232] <https://jira.csi.it/browse/NSP-1232>`_ - `[NSP-1212] <https://jira.csi.it/browse/NSP-1212>`_ - `[NSP-942] <https://jira.csi.it/browse/NSP-942>`_ - `[NSP-778] <https://jira.csi.it/browse/NSP-778>`_



.. _release-2.5.4:

Service Portal 2.5.4 (2022-02-11)
---------------------------------

**Changed**


*   Adeguamento per rilascio CMP Nivola 1.10.0
	
*   `[NSP-127] <https://jira.csi.it/browse/NSP-127>`_ - Master/Viewer di Account: visualizzazione tariffe e listino applicato all'Account


**Fixed**    
    

*   `[NSP-1050] <https://jira.csi.it/browse/NSP-1050>`_ - `[NSP-1094] <https://jira.csi.it/browse/NSP-1094>`_ 



.. _release-2.5.0:

Service Portal 2.5.0 (2021-10-12)
---------------------------------

**New**


*   `[NSP-753] <https://jira.csi.it/browse/NSP-753>`_ - Funzionalità di reboot VM
	
*   `[NSP-809] <https://jira.csi.it/browse/NSP-809>`_ - BackOffice: visualizzazione attributi WBS e Cliente Committente

**Changed**

*   `[NSP-273] <https://jira.csi.it/browse/NSP-273>`_ - Aggiunto ad "Account" attributo Cliente Pagante

*   `[NSP-578] <https://jira.csi.it/browse/NSP-578>`_ - Modifica matriche per licenze sistema operativo

*   `[NSP-842] <https://jira.csi.it/browse/NSP-842>`_ - Modifica csv risorse share/storage

*   `[NSP-792] <https://jira.csi.it/browse/NSP-792>`_ - Integrazione Api DBAAAS V2.0

**Fixed**    
    
*   `[NSP-839] <https://jira.csi.it/browse/NSP-839>`_ - Risoluzione bug creazione DBaaS Mysql

*   `[NSP-840] <https://jira.csi.it/browse/NSP-839>`_ - Risoluzione bug creazione DBaaS SQLServer

*   `[NSP-793] <https://jira.csi.it/browse/NSP-793>`_ - Risoluzione bug modifica flavour VM

*   `[NSP-813] <https://jira.csi.it/browse/NSP-813>`_ - Logout non più funzionante con SPID

*   `[NSP-871] <https://jira.csi.it/browse/NSP-871>`_ - `[NSP-799] <https://jira.csi.it/browse/NSP-799>`_ - `[NSP-807] <https://jira.csi.it/browse/NSP-807>`_ - `[NSP-808] <https://jira.csi.it/browse/NSP-808>`_ - `[NSP-845] <https://jira.csi.it/browse/NSP-845>`_ - `[NSP-842] <https://jira.csi.it/browse/NSP-842>`_


.. _release-2.4.0:

Service Portal 2.4.0 (2021-06-28)
---------------------------------

**New**

*   Gestione completa Volume Service (Beta). La funzionalità comprende:

    *   `[NSP-360] <https://jira.csi.it/browse/NSP-360>`_ - Creazione nuovo volume
	
    *   `[NSP-396] <https://jira.csi.it/browse/NSP-396>`_ - Elenco Volumi associati a VM
	
    *   `[NSP-361] <https://jira.csi.it/browse/NSP-361>`_ - Attach volume a VM
	
    *   `[NSP-395] <https://jira.csi.it/browse/NSP-395>`_ - Detach volume a VM
	
    *   `[NSP-589] <https://jira.csi.it/browse/NSP-589>`_ - Delete volume

*   `[NSP-655] <https://jira.csi.it/browse/NSP-655>`_ - Rimozione SG da istanza VM
    
*   `[NSP-658] <https://jira.csi.it/browse/NSP-658>`_ - Aggiunta SG a istanza VM

*   `[NSP-425] <https://jira.csi.it/browse/NSP-425>`_ - Funzionaità di BackOffice. Possibilità di allegare documenti di offerta e provisioning all'account

*   `[NSP-193] <https://jira.csi.it/browse/NSP-193>`_ - Elenco Shares - Visualizzazione colonna Tags

*   `[NSP-301] <https://jira.csi.it/browse/NSP-301>`_ - Disponibilità Report Csv con le risorse associate all'Account
    
**Changed**

*   `[NSP-289] <https://jira.csi.it/browse/NSP-289>`_ - Nuova gestione e icone per lo stato risorse

*   `[NSP-637] <https://jira.csi.it/browse/NSP-637>`_ - Ordinamento cronologia attività

*   `[NSP-550] <https://jira.csi.it/browse/NSP-550>`_ - Refactoring per visualizzazione 1366x768

*   `[NSP-707] <https://jira.csi.it/browse/NSP-707>`_ - Lista VM Account - tooltips su nome VM

*   `[NSP-638] <https://jira.csi.it/browse/NSP-638>`_ - Adeguamento interfaccia con aggiunta "Drill-Down" button su menu di navigazione

**Fixed**    
    
*   `[NSP-703] <https://jira.csi.it/browse/NSP-703>`_ - Elenco rendiconti account: mancata internazionalizzazione del mese

*   `[NSP-691] <https://jira.csi.it/browse/NSP-691>`_ - bug visualizzazione dettaglio account

*   `[NSP-517] <https://jira.csi.it/browse/NSP-517>`_ - problema visualizzazione Service Portal

*   `[NSP-610] <https://jira.csi.it/browse/NSP-610>`_ - Lista snapshot "Creation Date" : aggiungere ora e minuti

*   `[NSP-639] <https://jira.csi.it/browse/NSP-639>`_ - Bug Quote STAAS/SNAPSHOT

*   `[NSP-641] <https://jira.csi.it/browse/NSP-641>`_ - Viusalizzazione report mese in corso (Master Account)

*   `[NSP-642] <https://jira.csi.it/browse/NSP-642>`_ - presentazione Costi (Euro) nei report PDF

*   `[NSP-643] <https://jira.csi.it/browse/NSP-643>`_ - allineamento colonne report dettaglio pdf

*   `[NSP-648] <https://jira.csi.it/browse/NSP-648>`_ - Elenco ruoli compare solo voce (ruoli_elenco.Ospite)

*   `[NSP-649] <https://jira.csi.it/browse/NSP-649>`_ - bug tootip menu sinistro

*   `[NSP-336] <https://jira.csi.it/browse/NSP-636>`_ - `[NSP-644] <https://jira.csi.it/browse/NSP-644>`_ - `[NSP-645] <https://jira.csi.it/browse/NSP-645>`_ - `[NSP-650] <https://jira.csi.it/browse/NSP-650>`_ - `[NSP-667] <https://jira.csi.it/browse/NSP-667>`_



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


