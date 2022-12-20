.. _3_Cosa_sono_le_Region:

**Cosa sono le Region?**
************************

**Modello Multi-Region**
=========================

Nivola può essere ospitato in più locations in tutto il mondo. Queste locations sono composte da Region e
Availability Zones. Ogni Region è un'area geografica separata. Ogni Region ha più sedi isolate
note come Availability Zones. Nivola offre la possibilità di posizionare risorse, come istanze e dati
in più locations. Le risorse non vengono replicate tra le Region, a meno che non venga richiesto specificatamente.
Ogni Region è completamente indipendente. Ogni Availability Zones è isolata, ma le Availability Zones in una
Region sono connesse tramite collegamenti a bassa latenza. Il diagramma seguente illustra la relazione tra
Region e Availability Zones:

.. image:: img/relationshipRegion_AvZone.png


**Available Regions**
Le Region a disposizione sono determinate dall'account in uso.
La tabella seguente elenca le Region fornite da un account. Non è possibile accedere a Region esterne all'account in uso:

.. image:: img/Code_Name.jpg


**Regioni and Endpoint**
========================

Quando si lavora con un'istanza utilizzando l'interfaccia della riga di comando o tramite API, occorre specificare il relativo Regional Endpoint.
L'Endpoint del Piemonte è https://api.nivolapiemonte.it/




**Aree geografiche e zone**

Le aree geografiche sono aree geografiche indipendenti composte da zone. Le zone e le aree geografiche sono astrazioni logiche delle risorse fisiche sottostanti 
fornite in uno o più data center fisici. 
Una **zona** è un'area di deployment per le risorse all'interno di un'area geografica.
Le **Region** sono insiemi di zone. Le zone hanno connessioni di rete a bassa latenza e a larghezza di banda elevata con altre zone della stessa regione. 
Per eseguire il deployment di applicazioni a tolleranza di errore ad alta disponibilità, è consigliato di eseguire il deployment di applicazioni in più 
zone e in più aree geografiche. Ciò aiuta a proteggere dai guasti imprevisti dei componenti, fino a una zona o area geografica inclusa.
Le risorse Compute Engine sono ospitate in diverse località in tutto il mondo. Queste località sono composte di aree geografiche e zone. Una regione è 
una località geografica specifica in cui puoi ospitare le risorse. 
Le risorse che risiedono in una zona, come istanze di macchine virtuali o dischi a livello di zona, sono definite risorse di zona. Altre risorse, come 
indirizzi IP esterni statici, sono a livello di area geografica. Le risorse a livello di area geografica possono essere utilizzate da qualsiasi risorsa di 
quell'area, indipendentemente dalla zona, mentre le risorse di zona possono essere utilizzate solo da altre risorse della stessa zona.
Ad esempio, per collegare un disco permanente a livello di zona a un'istanza, entrambe le risorse devono trovarsi nella stessa zona. Analogamente, se si 
vuole assegnare un indirizzo IP statico a un'istanza, questa deve trovarsi nella stessa regione dell'indirizzo IP statico.
Collocando le risorse in zone diverse di un'area geografica si riduce il rischio di un'interruzione dell'infrastruttura che interessa contemporaneamente 
tutte le risorse. Collocando le risorse in diverse regioni si ottiene un livello ancora più elevato di indipendenza dagli errori. Questo consente di 
progettare sistemi robusti con risorse distribuite su diversi domini di errore.
Le risorse sono ospitate in più regioni. Ogni area geografica è composta da più zone. Le zone sono gruppi logici di risorse, progettati per evitare errori 
correlati. Collocare le risorse in più zone all'interno di un'area geografica riduce il rischio di errori correlati all'infrastruttura fisica e software 
che interessano le applicazioni. Collocando le risorse in aree geografiche diverse offre un livello ancora più elevato di indipendenza dagli errori.



**Scelta di una region e di una zona**

La scelta di un'area geografica e di una zona è importante per diversi motivi:


**Gestione degli errori**

Distribuire le tue risorse su più zone e aree geografiche serve a tollerare le interruzioni. Le zone sono progettate per ridurre al minimo il rischio di errori 
correlati causati da interruzioni dell'infrastruttura fisica, ad esempio alimentazione, raffreddamento o rete. Pertanto, se una zona non è più disponibile, 
è possibile trasferire il traffico in un'altra zona della stessa area geografica per mantenere i servizi in esecuzione. Allo stesso modo, è possibile mitigare 
l'impatto di un'interruzione della regione sulla tua applicazione eseguendo i servizi di backup in una regione diversa. 


**Latenza di rete ridotta**
Per ridurre la latenza di rete, è possibile scegliere un'area geografica o una zona vicina al proprio punto di servizio. 


