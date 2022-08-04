.. _Glossario:

<<<<<<< HEAD
**Termini ed Acronimi usati da Nivola**
=======================================

Nella tabella seguente, raggruppati in ordine alfabetico, si riportano i termini e gli acronimi frequentemente
utilizzati su Nivola, allo scopo di far acquisire
familiarità con la piattaforma.
=======
**Release Notes**
===================================
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

    1.1 [A]_

    1.2 [B]_

    1.3 [C]_

    1.4 [D]_

    1.5 [E]_

    1.6 [F]_

    1.7 [G]_

    1.8 [H]_

    1.9 [I]_

    1.10 [J]_

    1.11 [K]_

    1.12 [L]_

    1.13 [M]_

    1.14 [N]_

<<<<<<< HEAD
    1.15 [O]_

    1.16 [P]_
=======
.. _release-2.6.2:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

    1.17 [Q]_

    1.18 [R]_

    1.19 [S]_

    1.20 [T]_

    1.21 [U]_

<<<<<<< HEAD
    1.22 [V]_

    1.23 [W]_
=======
.. _release-2.6.1:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

    1.24 [X]_

    1.25 [Y]_

    1.26 [Z]_

--------

.. [A]

​1.1 A
--------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| ACCOUNT                              | Contenitore di istanze di servizio   |
|                                      | Per gli Account dell'Organizzazione  |
|                                      | CSI il nome con cui identificarlo è  |
|                                      | il **codice prodotto**.              |
|                                      | Per i prodotti del CSI è previsto un |
|                                      | Account per l'ambiente di produzone  |
|                                      | ed un altro per gli altri denominato |
|                                      | **preprod**.                         |
+--------------------------------------+--------------------------------------+
| API                                  | Application Programming              |
|                                      | Interface (in italiano traducibile   |
|                                      | come Interfaccia di programmazione   |
|                                      | di un'applicazione), le API sono     |
|                                      | strumenti di programmazione messi a  |
|                                      | disposizione degli sviluppatori per  |
|                                      | facilitare il loro compito nella     |
|                                      | realizzazione di applicazioni        |
|                                      | integrate.                           |
+--------------------------------------+--------------------------------------+
|                                      |                                      |
| APP Engine                           | Template preconfigurato composto da  |
|                                      | risorse elaborative, database,       |
|                                      | storage, reti e sicurezza che        |
|                                      | implementa una particolare funzione  |
+--------------------------------------+--------------------------------------+
| Availability Zone (AZ)               | Aggregato di uno o più Site. L’AZ è  |
|                                      | caratterizzata da una sua completa   |
|                                      | autonomia infrastrutturale e         |
|                                      | indipendenza                         |
+--------------------------------------+--------------------------------------+

-----------------------

.. [B]
​1.2​ B
--------------------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| BCKaaS                               | Il servizio di backup as a service è |
|                                      | un’opzione attivabile dall’utente    |
|                                      | per il backup delle macchine         |
|                                      | virtuali attivate in Nivola. Il      |
|                                      | Cliente può scegliere se attivare il |
|                                      | backup sulle risorse selezionate e   |
|                                      | scegliere i livelli di retention più |
|                                      | appropriati per il proprio servizio. |
|                                      |                                      |
|                                      | Il servizio viene erogato attraverso |
|                                      | piattaforme che permettono una       |
|                                      | notevole affidabilità                |
|                                      | infrastrutturale, e attraverso la    |
|                                      | funzione di “deduplica dei dati”,    |
|                                      | per  il raggiungimento di una        |
|                                      | elevata efficienza. I backup sono    |
|                                      | depositati su apparati storage       |
|                                      | differenti da quelli che ospitano    |
|                                      | dati e servizi .                     |
|                                      |                                      |
+--------------------------------------+--------------------------------------+

------------------------------


.. [C]

​1.3​ C
---------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Capability                           | Attributo essenziale dell'account per|
|                                      | istanziare i servizi. E' assegnato   |
|                                      | all'account in fase di creazione.    |
|                                      | A fronte di un account è possibile   |
|                                      | avere più capabilities.              |
+--------------------------------------+--------------------------------------+
| CLI                                  | Command Line Interface - nel         |
|                                      | progetto Nivola trattasi di command  |
|                                      | interface dedicata alla gestione di  |
|                                      | tutte le risorse della CMP.          |
|                                      | L’utilizzo è possibile anche per gli |
|                                      | utenti accreditati e i propri        |
|                                      | fornitori attraverso opportuna       |
|                                      | profilazione.                        |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| CMP                                  | Cloud Management Platform -          |
|                                      | piattaforma di integrazione ed       |
|                                      | automazione che espone tutti i       |
|                                      | servizi di business attraverso API   |
|                                      | (Application programming Interface)  |
|                                      | richiamabili dall’utente o           |
|                                      | attraverso l’uso del Service Portal. |
|                                      | Include i servizi di accounting,     |
|                                      | profilazione, security.              |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| Compute Services                     | Insieme di funzioni utili a creare e |
|                                      | gestire e le Virtual Machine         |
|                                      | Categoria di servizi che permette di |
|                                      | fruire di  risorse elaborative       |
|                                      | (espresse in CPU, RAM e spazio       |
|                                      | disco) in differenti flavour e       |
|                                      | template, corredate da servizi di    |
|                                      | networking e security.               |
|                                      |                                      |
|                                      | Sulla base del perimetro delle       |
|                                      | risorse presenti, gli utilizzatori   |
|                                      | saranno in grado di realizzare i     |
|                                      | propri tenant, istanziare le         |
|                                      | macchine virtuali selezionandole da  |
|                                      | un ampio catalogo di template e di   |
|                                      | gestirle in modo autonomo e          |
|                                      | integrato con gli altri servizi      |
|                                      | disponibili.                         |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| Consumer                             | User utilizzare della piattaforma    |
|                                      | Nivola                               |
+--------------------------------------+--------------------------------------+

-------

.. [D]

​
​1.4​ D

-------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Divisione                            | E' il secondo livello organizzativo. |
|                                      | Una organizzazione può avere più     |
|                                      | divisioni. Ogni Divisione ha         |
|                                      | ha associato un portafoglio chiamato |
|                                      | Wallet che ne definisce il limite    |
|                                      | di spesa. Per un Cliente esterno     |
|                                      | può coincidere con il valore della   |
|                                      | determina o con una pòarte di essa.  |
|                                      | Non può esserci una Divisione senza  |
|                                      | un Organizzazione da cui dipendere.  |
|                                      | Nel caso l'organizzazione della      |
|                                      | divisione sia CSI il suo nome        |
|                                      | dovrà coincidere sempre l'ID della   |
|                                      | Soluzione applicativa. Nel caso l'ID |
|                                      | non sia stato attrubuito usare       |
|                                      | "Staging" in attesa che venga        |
|                                      | attribuito                           |
+--------------------------------------+--------------------------------------+
| DBaaS                                | “Data Base as a Service” sono        |
|                                      | servizi gestiti  costituiti da       |
|                                      | ambienti virtuali dedicati  in       |
|                                      | differenti configurazioni e          |
|                                      | tecnologie, con differenti livelli   |
|                                      | di affidabilità e ridondanza in      |
|                                      | funzione delle esigenze del Cliente. |
|                                      | Sono inclusi i servizi di backup,    |
|                                      | restore, monitoraggio, aggiornamento |
|                                      | e patching.                          |
+--------------------------------------+--------------------------------------+


-----------

.. [E]

​1.5​ E
----------------------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+


-------------

.. [F]


​1.6​ F
-------------------
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| FLAVOUR Alias TYPE                   | Identificano le differenti tipologie |
|                                      | di VM le cui caratteristiche         |
|                                      | differiscono per la quantità di      |
|                                      | risorse CPU, RAM e DISCO. L’utente   |
|                                      | può scegliere tra diversi flavour in |
|                                      | base delle proprie esigenze.         |
+--------------------------------------+--------------------------------------+


<<<<<<< HEAD
----------------------
=======
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47


.. [G]

​1.7​ G
----------------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-----------------

.. [H]


​1.8​ H
------------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-----------------

.. [I]


​1.9​ I
--------------------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Immagine                             | Parametro che determina l'OS della VM|
|                                      | da istanziare eventualmente          |
|                                      | arricchito del software per          |
|                                      | l'automazione come p.e. ansible o    |
|                                      | heat                                 |
+--------------------------------------+--------------------------------------+

<<<<<<< HEAD
-----------------


.. [J]

=======
.. _release-2.5.4:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

​1.10​ J
------------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-----------------

.. [K]



​1.11 K
--------------
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| KEY                                  | Chiave ssh usata al momento della    |
|                                      | creazione della VM abilitando la     |
|                                      | connessione da remoto.               |
+--------------------------------------+--------------------------------------+


<<<<<<< HEAD
-------------------------

.. [L]

=======
.. _release-2.5.0:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

​1.12 L
--------
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-----------------

.. [M]


​1.1​3 M
--------------------
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-------------------------


.. [N]


​1.14 N
----------------
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Nivola                               | Ci si riferisce al complesso di      |
|                                      | tutte le componenti della            |
|                                      | piattaforma: Service Portal, CMP,    |
|                                      | back-end .                           |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| NMSF                                 | Nuovo Modello Server Farm            |
+--------------------------------------+--------------------------------------+
| NSC                                  | Nivola Support Center - Single Point |
|                                      | of Contact per tutti i servizi cloud |
|                                      | (Nivola, NMSF, POSC)                 |
|                                      |                                      |
+--------------------------------------+--------------------------------------+

-------------------------

.. [O]


​1.1​5 O
------------------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Organizzazione                       | E’ gerarchicamente il massimo livello|
|                                      | organizzativo. Dall'Organizzazione   |
|                                      | possono dipendere 1 o più Divisioni. |
|                                      | Ad un organizzazione può coincidere  |
|                                      | un Ente.  Il nome sarà sempre CSI    |
|                                      | per tutto ciò che dovrà ospitare     |
|                                      | prodotti del CSI.                    |
+--------------------------------------+--------------------------------------+

<<<<<<< HEAD
-------------------------

.. [P]
=======
.. _release-2.4.0:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47


​1.1​6 P
--------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Provider                             | CSI Piemonte, nella sua veste di     |
|                                      | Cloud provider                       |
+--------------------------------------+--------------------------------------+
| POD                                  | Point Of Delivery - aggregato di     |
|                                      | infrastrutture elaborative, storage, |
|                                      | rete e sicurezza autoconsistenti     |
+--------------------------------------+--------------------------------------+

-------------------------


.. [Q]



​1.17​ Q
----------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-----------------


.. [R]


1.18 R
--------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Region                               | Aggregato di una o più Availability  |
|                                      | Zone                                 |
+--------------------------------------+--------------------------------------+
| Rupar                                | Rupar Piemonte è la Rete Unitaria    |
|                                      | della Pubblica Amministrazione a cui |
|                                      | possono aderire tutti gli Enti       |
|                                      | locali piemontesi                    |
+--------------------------------------+--------------------------------------+

-------------------------


.. [S]


1.19 S
--------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| SG Security Group                    | E' il firewall della istanze di      |
|                                      | Nivola.                              |
|                                      | Configurabile dall'utente per        |
|                                      | controllare il traffico in entrata   |
|                                      | e in uscita da e verso le istanze.   |
|                                      | Il SG protegge ogni singola istanza  |
|                                      | al suo interno. Per far colloquiare  |
|                                      | istanze del medesimo SG tra loro     |
|                                      | si dovrà agire sulle regole          |
|                                      | di ingresso e di uscita.             |
+--------------------------------------+--------------------------------------+
| Service Portal                       | È il portale di servizio a cui       |
|                                      | consumer e provider accedono per il  |
|                                      | governo dei servizi esposti da       |
|                                      | Nivola. L’interfaccia è in grado     |
|                                      | cooperare con le API di business     |
|                                      | esposte dalla CMP.                   |
|                                      |                                      |
|                                      | Il Service Portal espone inoltre     |
|                                      | funzioni proprie come l’accesso alla |
|                                      | documentazione, ai video tutorial,   |
|                                      | alla chat e al Servizio di           |
|                                      | assistenza tramite il Team di        |
|                                      | Supporto Nivola per supportare       |
|                                      | l’utente in caso di problemi,        |
|                                      | malfunzionamenti o semplici          |
|                                      | how-to-use.                          |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| Site                                 | Aggregato di uno o più POD           |
+--------------------------------------+--------------------------------------+
| Storage as Service   STAAS           | Il servizio prevede la fornitura di  |
|                                      | spazio disco prestazionale           |
|                                      | raggiungibile via rete con           |
|                                      | protocolli NFS e CIFS esclusivamente |
|                                      | dalle macchine virtuali Nivola. La   |
|                                      | messa a disposizione dei servizi di  |
|                                      | storage avviene su infrastrutture    |
|                                      | ridondate e configurate in alta      |
|                                      | affidabilità.                        |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| SUBNET                               | E’ un range di IP utilizzabile       |
|                                      | all’interno del VpC. E’ possibile    |
|                                      | usare delle risorse di Nivola        |
|                                      | all’interno di una specifica subnet. |
|                                      | E’ possibile usare una subnet per    |
|                                      | risorse che devono connettersi ad    |
|                                      | Internet ed una privata, per risorse |
|                                      | che invece non hanno necessità di    |
|                                      | connettersi ad Internet.             |
|                                      | Per proteggere le risorse di Nivola  |
|                                      | in ciascuna sottorete, è possibile   |
|                                      | utilizzare più security groups.      |
+--------------------------------------+--------------------------------------+

-------------------------

.. [T]


1.20 T
-----------------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Tagli                                | Definiscono le dimensioni            |
|                                      | massime complessive delle risorse    |
|                                      | della Virtual Machine.               |
+--------------------------------------+--------------------------------------+
| Tags                                 | Attraverso i TAGS la piattaforma     |
|                                      | mette a disposizione                 |
|                                      | la possibilità di etichettare le     |
|                                      | proprie risorse in modo da facilitare|
|                                      | di individuarle e ricercarle con     |
|                                      | chiavi personalizzabili.             |
+--------------------------------------+--------------------------------------+
| Template                             | Sono le tipologie e le versioni del  |
|                                      | OS utilizzati per la creazione della |
|                                      | Virtual Machine.                     |
+--------------------------------------+--------------------------------------+

----------

.. [U]
​

1.21 U
----------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| Utente/User                          | Persona fisica accreditata           |
|                                      | all’accesso ai servizi Nivola        |
+--------------------------------------+--------------------------------------+

---------------


.. [V]



1.22 V
----------


+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
| VM: Virtual Machine                  | Server in grado di ospitare servizi. |
+--------------------------------------+--------------------------------------+
| VPC: Virtual Private Cloud           | E' una rete virtuale dedicata        |
|                                      | all’account Nivola, logicamente      |
|                                      | isolata dalle altre reti di Nivola.  |
|                                      | L’istanza è utilizzabie all’interno  |
|                                      | del proprio Vpc. Il Vpc è            |
|                                      | configurabile modificando il range   |
|                                      | degli indirizzi IP. Possibile creare |
|                                      | sottoreti, indicando route tables,   |
|                                      | network gateways e security settings.|
+--------------------------------------+--------------------------------------+

------------

.. [W]



1.23 W
----------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-------------


.. [X]


1.24 X
----------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+

-------------------


<<<<<<< HEAD
.. [Y]


1.25 Y
----------

+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
=======
.. _release-2.3.0:
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

-------------------------

.. [Z]


1.26 Z
----------

<<<<<<< HEAD
+--------------------------------------+--------------------------------------+
|            Acronimo/Termine          |            Significato               |
+--------------------------------------+--------------------------------------+
=======
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
>>>>>>> 40a2c27168b1249889ed4699b1e60aae87cf7e47

-------------------------

================================
