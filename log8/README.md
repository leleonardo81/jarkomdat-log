# Log 8 Jarkomdat

pembelajaran minggu ini tentang

## DHCP: Dynamic Host Configuration Protocol
Berbeda dengan static subnetting yang harus diassign secara statis / manual satu per satu, DHCP menyediakan pengassignan IP secara otomatis dan dinamis.

### proses pengassignan IP pada DHCP:
- host broadcast “DHCP discover” untuk mencari DHCP server
- DHCP server melakukan offer atau menawwarkan sebuah IP “DHCP offer” 
- kemudian host melakukan “DHCP request” ke DHCP server
- DHCP server mengirim alamat IP “DHCP ack”


nb:
- dengan DHCP IP yang digunakan tidak terbatas hanya yang dialokasikan seeprti ketika menggunakan static IP address