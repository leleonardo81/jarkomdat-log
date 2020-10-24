# Log 6 Jarkomdat

Minggu ini belajar tentang Network layer.  
ketika paket sudah dibentuk oleh transport layer (dibungkus), paket data akan didistribusikan ke jaringan untuk menentukan alamat ip sender dan receiever dari paket. 

### Fungsi utama network layer
- routing, melakukan penentuan alamat
- forwarding, mengirimkan data sesuai dengan alamat yang telah ditentukan

router membaca header dari paket data secara berurutan dari depan, lalu lanjut ke identifier selanjutnya dari data untuk dapat menentukan alamat tujuan dikirimnya paket data.

### Datagram network
biasa digunakan dalam transfer data dengan protokol udp di dalam network layer tidak ada inisiasi. paket dikirimkan langusung sesuai dengan addressnya, dan network layer hanya mengantarkan. tidak ada state dalam pengiriman karena yang penting hanya data dikirimkan tidak peduli data sudah sampai atau belum.


ada banyak jalan dalam melakukan forward data, maka network layer akan menentukan algoritma untuk memilih jalan yang sesuai untuk mengirirmkan paket data

paket dari transport layer  akan dibungkus lagi di network layer dengan identifier untuk: 
- sender / source
- receiever / destination
- version
- header length
- header checksum
- 16 bit identifier
- dll

karena paket dipecah pecah menjadi bentuk fragmentdan tidak selalu melalui path network yang sama. di destination, fragment akan digabungkan sesuai dengan urutan penyusunan yang ada di header dari paket yang dikirimkan di network layer. ini adalah salah satu kegunaan dari pembungkusan data dengan identifier-identifier pada network layer.

ip address sebenarnya adalah representasi dari 4 * 8 bits  binary. susunan ip address dibagi jadi 2 yaitu network dan host. 
proporsi susunan network address dan host  tidak selalu dibagi 2 rata (16-16) tapi bisa disesuaikan untuk efisiensi dari network dengan membagi ke subnet. Subnet yang besar akan dapat digunakan oleh banyak pengguna / host, karena subnetting memproposikan network untuk skala pengguna.

### subnetting 
ada 2 cara untuk melakukan subnetting: 
- static subnetting
- Variable Length subnet mask 

