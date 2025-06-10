
**Future releases**
===================

**Portale**
***********

*Versione 4.17.0*

*Data prevista*


|

**Cloud Management Platform**
*****************************

*Versione 1.17.6*

*Data prevista: giovedì 12 giugno*

*Bug fixing*

- Rimosso codice non usato (ServiceMetricConsume) deprecato 3 anni fa

- L'attributo delle istanze di Dbaas "allocated storage" utilizza il valore presente in configurazione e aggiornato durante la manutenzione

- Non è più esposto il valore calcolato dal componente resource in cui non sono presenti tutte le logiche di scorporamento delle risorse destinate ai dati da quelle per SO ed eventuali backup
    
- Corretta la gestione dello stato per le vm riportate da vcenter in stato "Crashed" 
    
- Corretta la gestione della cache per le risorse di tipo ComputeInstance che ora aggiornano la cache solo se sono state completamente inizializzate.
