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


