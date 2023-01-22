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

.. toctree::
    ../Overview_Nivola/2_Concetti_Base.rst#utenti-ruoli-ed-account

(parte del rischio: luca dice a ezio di aiutarmi)

(Luca dice “chiedere a gargano andrea” - verificare)





**Funzionalità per l'import e l'export dei dati**
=================================================

La funzionalità utilizzata per fare l’import di dati è quella relativa all'SFTP SERVER.
Per attivare tale funzionalità occorre contattare il supporto attraverso i consueti canali.

(in attesa di info da luigi favero su SFTP (chiedergli solo quello, come funziona))





**Interoperabilità e portabilità dei dati **
============================================

(in attesa di info da luigi favero su SFTP) + modalità camioncino ?

nota Eugenio: questo punto (più tecnico ma descrivere anche la funzionalità) e quello sopra ("Funzionalità per l'import e l'export dei dati", più procedurale) 
potrebbero essere trattati insieme, oppure come due paragrafi collegati

(le funzionalità sono disponibili e sono automatizzate. Per attivare il servizio occorre contattare il Supporto attraverso i consueti canali.