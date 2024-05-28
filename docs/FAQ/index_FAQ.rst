
**FAQ**
=======

- quali sono le immagini che eccedono, ad esempio, i 400Gb? Nessuna la configurazione è dinamica

- i boot delle immagini sono tutti di tipo BIOS? Sì

- ogni immagine contiene solo un disco MBR valido ed un boot loader? di default Sì

- il boot loader utilizza LVM o un UUID al volume di boot?  UUID

- il disco è criptato?  No

- l’immagine è di tipo VMDK o QCOW2 o comunque convertibile ad uno di questi formati?  vmdk per vsphere e qcow2

- le immagini sono state create da un clone o da snapshot?  Clone

- il VMDK consiste di un singolo file (single growable o stream optimized)? Singolo file

- l’interfaccia di rete utilizza DHCP? Sì per openstack, No per vsphere

- l’indirizzo IP e il MAC address sono definiti nel networking? Sì (vsphere)

- la VM ha uno storage remoto collegato?  Default no, su richiesta sì
