
**Future releases**
===================

**Portale**
***********

*Versione* 

*Data prevista*: 

|

**Cloud Management Platform**
*****************************

.. _release-1.16.9:

CMP Nivola 1.16.9 (2025-01-09)
------------------------------

*Nuove funzionalità/Improvement*

•  parametri per starter pack Oracle al provisioning di dbaas;
•  uso di orchestrator_tag al lancio delle customization;
•  aggiunta configurazione mailx e mount dei file system NFS per backup durante il provisioning di dbaas Oracle;
•  logging space ora cancella dashboard per vm, dbaas;
•  migrata cutomization os-utility2 su nuovi awx server;
•  gestione job_tags per awx nei module (logaas);
•  logging instance per dbaas ora aggiunge e cancella le dashboard


*Bug fixing*

•  fix errore cancellazione volume se None (NSP-3617)
•  fix metodo UpdateServiceConfigParamRequestSchema;
•  fix orchestrator enable_log_module;
•  fix add tag on creation;
•  aggiunto tag di backup per i dischi destinati ai buckup fisici in fase di creazione di dbaas Oracle;
