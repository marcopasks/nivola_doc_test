
**Future releases**
===================

**Portale**
***********

*Versione 4.1x*

*Data prevista: 

*Nuove funzionalità/Improvement*

*Bug fixing*

|

**Cloud Management Platform**
*****************************

*Versione 1.17.0*

*Data prevista: 27 febbraio 2025*

*Nuove funzionalità/Improvement*

•  Nuova gestione staas basata su on_tap
•  Aggiunta dettagli alle chiavi e ai nodi ssh nella gestione ssh
•  Il componente resource espone le api solo per chiamate interne o per utenti con privilegi amministrativi
•  Le capability gestiscono la data in cui sono state applicate in modo che sia possibile verificare se la capability è cambiata dopo che è stata assegnata/applicata ad un account
•  Modificate alcune tabelle per gestire attributi aggiuntivi
•  Aggiunte funzionalità per abilitare in ambienti di sviluppo la profilazione dei processi celery dei tasks asincroni, e dei processi uwsgi di esposizione api
•  Riscritte le api interne di crittografia per limitare le dipendenze e facilitare le build
•  Nuove logiche di gestione delle chiavi and key ssh e obbligatorietà delle chiavi su Linux
•  Nuova configurazione di awx e nuove logiche che permettono l'uso di diversi awx per sito
•  Ottimizzazioni di alcuni parametri per la creation di dbaas


*Bug fixing*

•  Alcuni comportamenti relativi a campi recentemente introdotti nella gestione degli utenti
•  Revisione commenti e riferimenti per la pubblicazione del codice
•  Comportamento della clonazione di macchine cross siti su openstack
•  Alcuni Timeout non dovuti
•  Invio di audit log da piattaforme di sviluppo
•  Molti schema openapi che non corrispondevano alla effettiva risposta dei metodi
•  Alcune caratteristiche della configurazione dei dbaas
•  Refactoring della configurazione dei server vsphere
•  Bug fixing minori
