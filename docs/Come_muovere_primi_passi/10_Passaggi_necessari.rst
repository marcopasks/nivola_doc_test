.. _Passaggi_necessari:

**Passaggi necessari**
======================


Per inizare a utilizzare la piattaforma **Nivola**
è necessario procedere seguendo i seguenti passaggi.

    1. :ref:`Processo di Accredito`
    2. :ref:`Completare i Livelli Organizzativi`
    3. :ref:`Attivare Utenti`
    4. :ref:`Verificare i VPC`
    5. :ref:`Verificare Security Group`
    6. :ref:`Creare i Servizi`
    7. :ref:`Strumenti di ausilio alla migrazione`


.. image:: img/Primi_Passi.png


.. _Processo di Accredito:

**Processo di Accredito**
=========================

Per poter utilizzare i servizi esposti dalla piattaforma Nivola è necessario accreditarsi secondo il seguente processo:


    1. Contattare il proprio account di riferimento o andare alla sezione Contatti
       raggiungibile dal sito www.nivolapiemonte.it. Una volta attivato il
       contratto o l'utilizzo del servizio in modalità "Demo",
       il Team di Supporto Nivola provvederà a contattare il referente del
       Cliente per procedere con la creazione delle prime credenziali di accesso.
    2. Dopo avere ricevuto l’offerta ufficiale protocollata, procedere
       con l’emissione di un ordine al CSI-Piemonte.
    3. Approvare e impegnare con una determina l’importo presente nell’offerta.
    4. Inviare la documentazione tramite PEC all’indirizzo protocollo@cert.csi.it
       indicando nell’oggetto dell’email:
        a) Attivazione Servizi Nivola.
        b) Numero di protocollo presente sull’offerta.
        c) Nome dell’Ente.
    5. Indicare un referente che sarà contattato dal nostro servizio di assistenza per i dettagli tecnici. Nel caso in cui  la persona cui rivolgersi, in caso di incident di sicurezza, sia diversa da quella indicata in precedenza, serve individuare un nominativo diverso, in ottemperanza alle norme di ultima introduzione in ambito di Data Breach.



Questi aspetti sono riportati nel manuale utente del servizio e nelle condizioni generali in cui è possibile trovare
maggiori dettagli e informazioni anche inerenti la cessazione del servizio. Nel caso si presentasse questa evenienza
 il CSI si impegna a mettere a disposizione del Cliente i propri dati e successivamente di cancellarli.

.. image:: img/Richiesta_accredito.png


Terminata la fase di richiesta si
riceverà dal Team di Supporto la comunicazione via e-mail del **primo accredito**.
In questo modo l'utente,
sarà in grado di controllare la struttura organizzativa modellata dal Supporto e
conferire ulteriori abilitazioni.



.. _Completare i Livelli Organizzativi:

**Completare i Livelli Organizzativi**
======================================

La piattaforma si compone di 3 livelli organizzativi quello deputato ad ospitare i servizi è
l'**account**.  Nel caso, l'**account** non fosse stato definito dal supporto, prima di crearlo sarà indispensabile
individuare o creare una **Divisione** da cui farlo dipendere. La presenza dell'**Organizzazione**
e della **Divisione** sono la condizione necessaria alla generazione dell'**account**.


.. _Attivare Utenti:

**Attivare Utenti**
===================

Successivamente ad aver costituito la struttura organizzativa,
sarà possibile indicare a **Nivola** gli **utenti** associati a **ruoli**
che ad ogni livello, potranno agire sugli oggetti con compiti specifici.


.. _Verificare i VPC:

**Verificare i VPC**
======================

Dopo la creazione dell'Account e l'associazione delle utenze al profilo organizzativo corretto
è da verificare la corretta configurazione dei propri **VPC (Virtual Private Clud)**. All'interno
dei propri VPC l'utente potrà gestire e configurare le proprie risorse. Il **VPC**
garantisce il necessario isolamento tra le varie organizzazioni.

.. _Verificare Security Group:

**Verificare Security Group**
=============================

Nivola mette a disposizione alcuni SG pre-configurati ma è possibile
modificarne le regole o creare nuovi SG in funzione delle specifiche esigenze.
E' importante quindi verificarli ed eventualmente modificarli o integrarli
prima di iniziare a creare i Servizi. Sarà in ogni caso sempre possibile
modificare le regole di sicurezza anche successivamente alla creazione dei Servizi
ma non è possibile spostare un Servizio da un SG ad un altro dopo la creazione. In questo caso sarà necessario
distruggere il Servizio e ricrearlo nel SG corretto.


.. _Creare i Servizi:

**Creare i Servizi**
====================
Dopo aver concluso i passaggi precedenti sarà possibile iniziare la creazione
dei servizi tramite l'apposito menù del Service Portal. Il processo di creazione
è sempre guidato attraverso un apposito wizard di creazione. Il processo può
sempre essere interrotto prima della conferma finale ed è possibile
accedere direttamente alla presente guida per maggiori informazioni.



.. _Strumenti di ausilio alla migrazione:

**Strumenti di ausilio alla migrazione**
========================================
Dopo aver concluso i passaggi precedenti sarà possibile iniziare la creazione
dei servizi tramite l'apposito menù del Service Portal. Il processo di creazione
è sempre guidato attraverso un apposito wizard di creazione. Il processo può
sempre essere interrotto prima della conferma finale ed è possibile
accedere direttamente alla presente guida per maggiori informazioni.

**Migrazione VM**

Import
^^^^^^

**Import da server openstack**

Creazione provider instance:

.. code-block:: bash


    $ beehive res-provider instance-import tst-wf1-emood2-bck 720825e5-5472-44d5-970f-fd7702527386 passw0rd 46ea8662-94a1-496a-9a64-73342d4e2c06 primachiave-key-emood2-preprod


Registrazione provider instance nel modulo ssh per abilitare la connessione utente via ssh:

.. code-block:: bash


    $ beehive res-provider instance-manage e19f0137-bf0d-4e0a-8be3-c0f9e35fbc54 primachiave-key-emood2-preprod


Creazione del servizo utente nell’account:

.. code-block:: bash


beehive bu service-insts import-from-resource tst-wf1-emood2-bck emood2-preprod ComputeInstance ComputeService e19f0137-bf0d-4e0a-8be3-c0f9e35fbc54 -service_definition_id a9d1b6c0-bf72-4d6a-b780-feb5f3f6f7f5


**Lista sistemi operativi supportati per Import da server vsphere per rehosting:**

RedhatLinux7, GisMasterWin2016, Oracle11EE, NuvolaWebWin2016, Oracle19EE, Oracle12EE, Oracle12, Oracle11, mssql2017, windows2019, 
windows2012, windows2016, oracle12-test, Centos7.2-Oracle




**Migrazione DBAAS**

Import
^^^^^^

**Import da server openstack**

Creazione provider instance:

.. code-block:: bash


    $ beehive res-provider instance-import dbs-emood2-tst-bck-001m-server01 0ef13cc2-1d47-45ee-ae9d-2d06ccb7839a passw0rd 46ea8662-94a1-496a-9a64-73342d4e2c06 opstkcsi-podto2


Registrazione provider instance nel modulo ssh per abilitare la connessione utente via ssh:

.. code-block:: bash


    $ beehive res-provider instance-manage 864f8b9d-522a-4328-8e4b-564873418018 opstkcsi-podto2


Disabilitazione calcolo quote e metriche della provider instance:

.. code-block:: bash


    $ beehive res entities disable-quotas 864f8b9d-522a-4328-8e4b-564873418018


Creazione provider sql stack v2:

.. code-block:: bash


    $ beehive res-provider stack-sql-import dbs-emood2-tst-bck-001m dbs-emood2-tst-bck-001m-server01 mysql 5.7.23 '<pwd dbms>'


Creazione del servizio utente nell’account:

.. code-block:: bash


    $ beehive bu service-insts import-from-resource dbs-emood2-tst-bck-001m emood2-preprod DatabaseInstance DatabaseService 04f4e790-9529-4e9c-899a-4036113744b5

