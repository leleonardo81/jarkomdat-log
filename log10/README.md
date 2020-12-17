# Week 10 - Ethernet & Vlan

setiap host dalam network memiliki 2 address untuk link layer (mac address) dan network layer (IP address). Karena ada 2 address ini ada kebutuhan untuk mentranslate alamat yaitu dengan Address Resolution Protocol (ARP). 

Ethernet Physical Topology:
- Bus:  semua host terhubung ke kabel coaxial Langsung. (bisa collide satu sama lain)
- Star: semua host terhubung ke switch yang aktif ditengah.

Ethernet bekerja di link layer dengan mengirimkan datagram sebagai frame. Ethernet bersifat connectionless, dan unreliable. connectionless bearti tidak ada handshacking antar NIC penerima dan pengirim.  Unreliable bearti data tidak dijamin keutuhannya, penanganan data yang hilang harus dari layer diatasnya.

Salah satu link layer device yang sering digunakan adalah Switch. Berbeda dengan router yang merupakan network layer device, Switch ini ada secara fisik sbagai device penghubung pada link layer, walaupun secara logic dapat diabaikan karena host tidak mengetahui keberadaan device ini. 

Setiap switch memiliki forwarding table sendiri untuk dapat mengenali host mana saja yang terhubung dengannya karena mempunyai kemampuan self-learning untuk mengidentifikasi host. nantinya paket data yang datang akan diforward ke alamat yang sesuai. 

### VLAN
kita dapat membagi host-host ke dalam LAN yang berbeda beda. Jika kita ingin memisahkan beberapa group of host ke LAN yang berbeda, maka kita dapat melakukannya dengan VLAN. Switch device memiliki kemampuan untuk dapat melakukan configurasi multiple vlan. Vlan pada switch ditentukan berdasarkan port pada switch. kita dapat melakukan konfigurasi port untuk mengkonfigurasi vlan pada switch. Nantinya port-port yang berbeda vlan akan beroperasi seakan akan menjadi switch yang berbeda, walau secara fisik hanya satu switch. 

Dengan adanya vlan kita dapat merestrict koneksi antar LAN yang berbeda. dan menyediakan LAN yang khusus dengan fungsi dan keperluan masing masing, misal pembagian LAN pada divisi yang berbeda di pabrik. 

--- 
Multiprotocol label switching (MPLS): high-speed IP forwarding using fixed length label (instead of IP address), adalah protokol IP forwarding yang lebih cepat dari protokol yang sebelumnya sudah dipelajari. 
