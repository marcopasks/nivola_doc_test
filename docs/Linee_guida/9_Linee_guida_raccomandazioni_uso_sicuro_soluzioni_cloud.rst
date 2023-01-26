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

Tale modalità di accesso è duplicata anche per l’accesso ai db instance, facendo ricorso ai tool di database management e all'utilizzo 
delle chiavi private

.. image:: img/SSH_Gateway1.jpg

.. image:: img/SSH_Gateway2.jpg

.. image:: img/SSH_Gateway3.jpg

.. image:: img/SSH_Gateway4.jpg


**Connessione DB con DBeaver Mysql**

•	Aprire DBeaver
•	Cliccare sull’icona della spina col + e selezionando il DB desiderato

.. image:: img/Connessione-DB-con-DBeaver-Mysql1.png

•	Inserire IP, porta, utente e password del DB


.. image:: img/Connessione-DB-con-DBeaver-Mysql2.png

•	Scheda SSH, inserire flag Use SSH Tunnel, nel pannello Host inserire cmpto2-gw02.site02.nivolapiemonte.it se l’utente è un utente interno CSI, inserire cmpto2-gw01.site02.nivolapiemonte.it se l’utente è un utente Fonitore. Su User Name mettere la propria matricola CSI nel relativo campo oppure l’utenza nome.cognome@fornitori.nivola e la relativa password.

.. image:: img/Connessione-DB-con-DBeaver-Mysql3.png

•	Cliccare Fine, ora la configurazione sarà presente nella pagina principale e ci si potrà collegare cliccandoci






**Connessione DB con DBeaver Oracle**

•	Aprire DBeaver
•	Cliccare sull’icona della spina col + e selezionando il DB desiderato

.. image:: img/Connessione-DB-con-DBeaver-Oracle1.png

•	Inserire IP, porta, utente e password del DB

.. image:: img/Connessione-DB-con-DBeaver-Oracle2.png

•	Scheda SSH, inserire flag Use SSH Tunnel, nel pannello Host inserire cmpto2-gw01.site02.nivolapiemonte.it,su User Name mettere la propria matricola CSI e Password nel relativo campo

.. image:: img/Connessione-DB-con-DBeaver-Oracle3.png

•	Cliccare Fine, ora la configurazione sarà presente nella pagina principale e ci si potrà collegare cliccandoci






**Connessione DB con DBeaver**

•	Aprire DBeaver
•	Cliccare sull’icona della spina col + e selezionando il DB desiderato

.. image:: img/Connessione-DB-con-DBeaver1.png

•	Inserire IP, porta, utente e password del DB

.. image:: img/Connessione-DB-con-DBeaver2.png

•	Scheda SSH, inserire flag Use SSH Tunnel, nel pannello Host inserire cmpto2-gw02.site02.nivolapiemonte.it se l’utente è un utente interno CSI, inserire cmpto2-gw01.site02.nivolapiemonte.it se l’utente è un utente Fonitore ,su User Name mettere la propria matricola CSI nel relativo campo oppure l’utenza nome.cognome@fornitori.nivola e la relativa password.

.. image:: img/Connessione-DB-con-DBeaver3.png

•	Cliccare Fine, ora la configurazione sarà presente nella pagina principale e ci si potrà collegare cliccandoci


**Configurazione WinScp**

•	Aprire WinScp -> Nuovo sito

.. image:: img/Configurazione_WinScp1.png

•	Inserire IP vm destinazione, utente e password

.. image:: img/Configurazione_WinScp2.png

•	Avanzate… -> Connessione -> tunnel 
Inserire flag Connetti usando tunnel SSH, Nome host cmpto2-gw01.site02.nivolapiemonte.it, Nome Utente (matricola) e password 
oppure Nome Utente (nome .cognome@fornitori.nivola) e password in caso di Enti

.. image:: img/Configurazione_WinScp3.png

•	Cliccare OK


**Connessione diretta SSH VM cloud**

•	Session

.. image:: img/Connessione-diretta-SSH-VM-cloud1.png

•	SSH

.. image:: img/Connessione-diretta-SSH-VM-cloud2.png

•	IP server di destinazione e utente root

.. image:: img/Connessione-diretta-SSH-VM-cloud3.png

•	Network settings (settare cmpto2-gw02.site02.nivolapiemonte.it, vostra matricola csi)

.. image:: img/Connessione-diretta-SSH-VM-cloud4.png


**Connessione diretta VM**

Creare il tunnel SSH
--------------------

•	Aprire Putty

.. image:: img/Connessione-diretta-VM1.png

•	Impostare come host name cmpto2-gw01.site02.nivolapiemonte.it oppure IP 10.138.154.13 

.. image:: img/Connessione-diretta-VM2.png

•	Nella sezione Connection  Data in Auto-login username, impostare: nome.cognome@fornitori.nivola 

.. image:: img/Connessione-diretta-VM3.png

•	Nella sezione Connection  SSH cliccare su + per espandere 

.. image:: img/Connessione-diretta-VM4.png

•	Nella sezione Connection  SSH  Auth click su Browse… ed impostare la chiave SSH assegnata 

.. image:: img/Connessione-diretta-VM5.png

•	Nella sezione Connection  SSH  Tunnels impostare Source port 2222 e come destination l’IP della macchina da raggiungere desiderata :22 e cliccare su Add

.. image:: img/Connessione-diretta-VM6.png

•	Tornare alla sezione Session su Saved Sessions dare un nome significativo e cliccare Save 

.. image:: img/Connessione-diretta-VM7.png

•	Ripetere i passaggi precedenti per aggiungere ulteriori VM che volete raggiungere, ricordandosi di incrementare ogni volta la Source port sotto Connection -> SSH -> Tunnels


Creare le connessioni
---------------------

•	Selezionare Default Settings e cliccare Load, compilare il campo Host Name con 127.0.01 e Port 2222 

.. image:: img/Connessione-diretta-VM8.png

•	Nella sezione Connection -> Data in Auto-login username, impostare: root 

.. image:: img/Connessione-diretta-VM9.png

Nella sezione Connection -> SSH -> Auth click su Browse… ed impostare la chiave SSH assegnata 

.. image:: img/Connessione-diretta-VM10.png

•	Tornare alla sezione Session su Saved Sessions dare un nome significativo relativo alla VM da raggiungere e cliccare Save 

.. image:: img/Connessione-diretta-VM11.png

•	Ripetere i passaggi precedenti per aggiungere ulteriori VM che volete raggiungere, ricordandosi di incrementare ogni volta il numero della porta configurato precedentemente


Connessione SSH
---------------

•	Effettuati questi passaggi rimane solamente la fase di connessione, dalla pagina Sessions di putty fate doppio click sulla sessione creata ad inizio della guida 

.. image:: img/Connessione-diretta-VM12.png

•	Si aprirà una shell simile a questa, lasciatela aperta

.. image:: img/Connessione-diretta-VM13.png

•	Infine aprire un nuovo putty, doppio click sulla connessione creata nella seconda parte di guida e vi collegherete all VM desiderata

.. image:: img/Connessione-diretta-VM14.png

•	Ogniqualvolta vorrete collegarvi a questa macchina dovrete effettuare solamente la parte Connessione SSH di questo manuale
•	A fine sessione ricordarsi di chiudere anche la connessione putty creata precedentemente    


Trasferimenti SFTP
------------------

•	Scaricate ed installate WinSCP, durante l’installazione vi chiederà se importare le sessioni da putty, se invece lo avete già installato seguite i seguenti passi:
•	Strumenti --> Importa siti

.. image:: img/Connessione-diretta-VM15.png

•	Selezionare le sessioni create precedentemente che puntano alla macchina locale [127.0.0.1] e fate click su OK

.. image:: img/Connessione-diretta-VM16.png

•	A questo punto dopo aver aperto la sessione a cmpto2-gw01.site02.nivolapiemonte.it da putty, cliccate Accedi sulla sessione relativa WinSCP e avrete la connessione SFTP con la VM 

.. image:: img/Connessione-diretta-VM17.png

•	A fine sessione ricordarsi di chiudere anche la connessione putty


**Connessione con tunnel ssh**

Creare il tunnel SSH
--------------------

•	Aprire Putty

.. image:: img/Connessione-tunnel-ssh-domnt1.png

•	Impostare come host name cmpto2-gw02.site02.nivolapiemonte.it oppure IP 10.138.154.14 

.. image:: img/Connessione-tunnel-ssh-domnt2.png

•	Nella sezione Connection  Data in Auto-login username, impostare matricola DOMNT

.. image:: img/Connessione-tunnel-ssh-domnt3.png

•	Nella sezione Connection  SSH cliccare su + per espandere 

.. image:: img/Connessione-tunnel-ssh-domnt4.png

•	Nella sezione Connection  SSH  Tunnels impostare Source port ad esempio 2222 e come destination l’IP della macchina da raggiungere desiderata e 
la relativa porta e cliccare su Add

.. image:: img/Connessione-tunnel-ssh-domnt5.png

•	Tornare alla sezione Session su Saved Sessions dare un nome significativo e cliccare Save 

.. image:: img/Connessione-tunnel-ssh-domnt6.png

•	Ripetere i passaggi precedenti per aggiungere ulteriori VM che volete raggiungere, ricordandosi di incrementare ogni volta la Source port sotto Connection  SSH  Tunnels
Apertura connessione
•	Doppio click da putty sulla sezione configurata in precedenza
•	Aprire il client DB o browser e puntare all’ip porta locali configurati ad esempio 127.0.0.1:2222


**Connessione con tunnel ssh**

Creare il tunnel SSH
--------------------

•	Aprire Putty

.. image:: img/Connessione-con-tunnel-ssh1.png

•	Per gli utenti esterni al CSI Piemonte e che non dispongono di credenziali di dominio devono procedere con questa impostazione: host name 
cmpto2-gw01.site02.nivolapiemonte.it oppure IP 10.138.154.13 ; 

.. image:: img/Connessione-con-tunnel-ssh2.png

•	Nella sezione Connection  Data in Auto-login username, impostare 
o	Nella sezione Connection  Data in Auto-login username, impostare nel caso di utenti esterni al CSI Piemonte e che non dispongono di credenziali di dominio, 
le credenziali nome.cognome@fonitori.nivola e relativa password

.. image:: img/Connessione-con-tunnel-ssh3.png

•	Nella sezione Connection  SSH cliccare su + per espandere 

.. image:: img/Connessione-con-tunnel-ssh4.png

•	Nella sezione Connection  SSH  Tunnels impostare Source port ad esempio 2222  e come destination l’IP della macchina da raggiungere desiderata e la 
relativa porta e cliccare su Add

.. image:: img/Connessione-con-tunnel-ssh5.png

•	Tornare alla sezione Session su Saved Sessions dare un nome significativo e cliccare Save 

.. image:: img/Connessione-con-tunnel-ssh6.png

•	Ripetere i passaggi precedenti per aggiungere ulteriori VM che volete raggiungere, ricordandosi di incrementare ogni volta la Source port sotto Connection  SSH  Tunnels
Apertura connessione
•	Doppio click da putty sulla sezione configurata in precedenza e lasciare la sessione aperta con NO SHELL
•	Aprire una seconda sessione e puntare all’ip porta locali configurati ad esempio 127.0.0.1:2222


**SSH tunnel on Toad**

.. image:: img/SSH-tunnel-on-Toad1.png




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
