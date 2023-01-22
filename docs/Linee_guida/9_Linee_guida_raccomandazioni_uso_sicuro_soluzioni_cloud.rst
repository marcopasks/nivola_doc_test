.. _Linee_guida_raccomandazioni_uso_sicuro_soluzioni_cloud:

**Linee guida e raccomandazioni sull’uso sicuro di soluzioni cloud**
====================================================================

**Istruzioni per una configurazione sicura**
********************************************

.. toctree::
    ../Come_fare_per/11.5_Gestione_chiavi_ssh.rst
    ../Come_fare_per/15.3_Template_Sicurezza.rst


Load balancer
-------------

L’obiettivo è di separare la componente di erogazione del servizio dall’esposizione:  

la sicurezza viene garantita attraverso il disaccoppiamento tra il mondo internet e la rete privata, e tra la rupar e la rete privata.

Inoltre il bilanciatore ha l'obiettivo di ripartire il carico su più elementi per aumentare la resilienza del servizio.

Nel caso in cui ci sia una sola VM si applica il Natting: viene utilizzato un IP pubblico che espone una solo macchina e occorre effettuare il bilanciamento.
Vi è un rapporto di 1:1 tra IP pubblico e VM, al contrario con il bilanciatore il rapporto è di 1 a molti


.. image:: img/Load-BalancerLS.drawio.png

Per attivare il servizio occorre contattare il Supporto attraverso i consueti canali.



**Gestione degli errori e meccanismi di logging**
*************************************************

.. toctree::
    ../Come_fare_per/30.7_Servizio_di_Log_Management.rst



**Meccanismi  di autenticazione**
*********************************

.. toctree::
    ../Usare_Cli/index_Usare_Cli.html

SSH Gateway
-----------

L'SSH Gateway risponde a URL differenti (a seconda della tipologia di cliente). Attraverso un client SSH si apre una sessione SSH utilizzando 
una user e una password (associati a LDAP). Dall'SSH Gateway si configura un tunnel sulla VM, poi attraverso lo stesso client SSH in modalità terminal 
emulator ci si collega alla porta configurata ed infine ci si collega sulla macchina. L'attività viene quindi effettuata in due passaggi.

.. image:: img/SSH_Gateway1.jpg

.. image:: img/SSH_Gateway2.jpg

.. image:: img/SSH_Gateway3.jpg

.. image:: img/SSH_Gateway4.jpg




**Servizi e funzioni per l'amministrazione del servizio da parte di utenti privilegiati / Ruoli e diritti, comprese le combinazioni che risultano in un rischio elevato**
*************************************************************************************************************************************************************************

Utenti, ruoli ed Account
------------------------

Si possono distinguere più ruoli all’interno della piattaforma, che si
correlano alla struttura organizzativa definita. Ad ogni ruolo può
corrispondere almeno un utente, e quindi almeno una persona fisica che
svolge quella funzione. Una persona registrata sul sistema può essere
associata a più ruoli anche su strutture organizzative differenti. Ad
esempio un utente può avere ruoli differenti su account anche di
divisioni distinte.

Ad oggi all’interno del sistema sono implementati i seguenti ruoli
utente.

**Master di Organizzazione**: questo ruolo rappresenta gli utenti che
possono svolgere funzioni amministrative all’interno dell’Organizzazione
quali la creazione, sempre all’interno dell’organizzazione di
pertinenza, delle divisioni e degli account; può inoltre profilare gli
utenti per renderli operativi all’interno della propria struttura ed
eventualmente registrare utenti non ancora presenti sulla piattaforma.
Il Master di Organizzazione può monitorare i costi e lo stato delle
risorse a tutti i livelli della propria struttura organizzativa
(divisioni e account) e visualizzarne i relativi report. Non ha però
accesso alle funzioni di gestione (creazione/modifica/cancellazione)
delle risorse associate agli account della propria organizzazione.

**Master di Divisione**: questo ruolo rappresenta gli utenti che possono
svolgere funzioni amministrative all’interno della Divisione quali la
creazione, sempre all’interno della divisione di pertinenza, degli
account; può inoltre profilare gli utenti per renderli operativi
all’interno della propria struttura ed eventualmente ha la possibilità
di registrare utenti non ancora presenti sulla piattaforma. Il Master di
Organizzazione può monitorare i costi e lo stato delle risorse a tutti i
livelli della propria struttura organizzativa (account) e visualizzarne
i relativi report. Non ha però accesso alle funzioni di gestione
(creazione/modifica/cancellazione) delle risorse associate agli account
della propria divisione.

**Amministratore di Back Office**: utente che all’interno del sistema ha
privilegi sulle funzioni di BackOffice (registrazione nuovi Utenti,
Accreditamento, creazione livelli organizzativi) e monitoraggio costi e
stato della piattaforma. L’Amministratore di BackOffice può profilare
utenti con ruoli a qualsiasi livello della struttura organizzativa. Può
inoltre accedere ai report dei costi e consumi aggregati a qualsiasi
livello. Il ruolo è solitamente associato a utenti dei gruppi di
gestione e supporto Csi Piemonte.

**Master di Account**: utente che all’interno dell’Account può gestire
tutte le risorse, sulle quali ha quindi il massimo dei privilegi. Il
Master di Account può quindi creare/cancellare/modificare le risorse,
può anche gestire le risorse create da altri utenti nell’account. Il
Master di Account può visualizzare e accedere ai report dei costi e dei
consumi relativamente al proprio account. Il master di account può
registrare nuovi utenti all’interno del proprio account e può
profilare o revocare utenti già censiti ad accedervi.

**Viewer di Account**: utente che all’interno dell’Account può visualizzare
tutte le risorse, sulle quali non ha però privilegi di modifica/cancellazione.
Il Viewer di Account può quindi visualizzare l'elenco dei servizi attivi
sull'Account , può visualizzarne il dettaglio, ma non ha possibilità 
di attivarne di nuovi e modificarne lo stato. 
Il Viewer di Account può visualizzare e accedere ai report 
dei costi e dei consumi aggregati dell'account. Il Viewer di account non può
registrare nuovi utenti all’interno della piattaforma e non può
profilare altri utenti ad accedervi.

La fase di introduzione di un nuovo utente si articola in questo modo:
un master, nel limite dei privilegi del suo livello gerarchico, può
accreditare un utente registrato sulla piattaforma assegnandogli un
ruolo, in questo modo gli concede dei permessi per svolgere determinate
funzioni che faranno ricadere il nuovo utente in un determinato gruppo.

La stessa operazione può essere effettuata e delegata all’operatore di
Backoffice.

Riassumendo:

-  Un Master di Organizzazione può :ref:`accreditare o revocare utenti <Creare_Accreditare_Utente>`
   all’interno delle proprie divisioni o account

-  Un Master di Divisione può :ref:`accreditare o revocare utenti <Creare_Accreditare_Utente>` all’interno
   dei propri account e della propria divisione.

-  Un Master di Account può :ref:`accreditare o revocare utenti <Creare_Accreditare_Utente>` all’interno
   del proprio account.
   
-  L’Amministratore di Backoffice può :ref:`accreditare o revocare ruoli <Creare_Accreditare_Utente>` agli
   utenti a qualsiasi livello della struttura gerarchica.



(parte del rischio: luca dice a ezio di aiutarmi)

(Luca dice “chiedere a gargano andrea” - verificare)





**Funzionalità per l'import e l'export dei dati**
=================================================

La funzionalità utilizzata per fare l’import di dati è quella relativa all'SFTP SERVER.
Per attivare tale funzionalità occorre contattare il supporto attraverso i consueti canali.

(in attesa di info da luigi favero su SFTP (chiedergli solo quello, come funziona))





**Interoperabilità e portabilità dei dati**
===========================================

(in attesa di info da luigi favero su SFTP) + modalità camioncino ?

nota Eugenio: questo punto (più tecnico ma descrivere anche la funzionalità) e quello sopra ("Funzionalità per l'import e l'export dei dati", più procedurale) 
potrebbero essere trattati insieme, oppure come due paragrafi collegati

(le funzionalità sono disponibili e sono automatizzate. Per attivare il servizio occorre contattare il Supporto attraverso i consueti canali.