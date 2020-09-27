# LOG minggu 2 Jarkomdat

### Leonardo 1806191023
### Jarkomdat - A
---

**Network Core** adalah Kumpulan Router yang terkoneksi satu sama lain dalam sebuah jaringan besar.


cara kerja router dengan packet switching:
1. Store:  router menerima data dalam bentuk paket dan disimpan sementara di router
2. Queueing: paket yang masuk akan diantrikan untuk selanjutnya diproses oleh router.
3. Routing: paket yang disimpan dibungkus dengan bit yang menyatakan jalur yang dilalui paket untuk sampai tujuan. 
4. Forwarding: router mengirim data ke router selanjutya untuk diforward lagi sampai tujuan.

cara kerja circuit switching:
1. **Time Divison MultiPlexing (TDM)** Circuit Switching dengan mendedikasikan jalur komunikasi dibagi berdasarkan waktu.
2. **Frequency Division Multiplexing (FDM)** Circuit Switching dengan mendedikasikan jalur komunikasi dibagi berdasarkan frekuensi.


Internet dapat terhubung dengan jaringan jaringan di seluruh dunia melalui ISP (Internet Service Provider). ISP ISP ini juga terbagi bagi menjadi Tingkatan atau Tier:
- Tier 1: ISP Global yang menghubungkan ISP antar benua atau antar negara.
- Tier 2: ISP yang menjadi Exchange point dari jaringan antar ISP
- Tier 3: ISP yang langsung terkoneksi ke pengguna, rumah, kantor dll untuk memberikan akses internet bagi pengguna.

ada pula:
- Regional ISP: ISP yang mencakup suautu wilayah tertentu secara geografis
- Content Provider Network: Private network khusus yang menyambungkan data center ke internet, contohnya *google*.
- Internet Exchange Point: exchange point bagi ISP agar terhubung dengan ISP lainnya

___
**Internet Protocol Stack** terdiri dari: 
1. **Application**: Mendukung aplikasi yang menggunakan jaringan, dengan protokol HTTP, SMTP, FTP dll
2. **Transport**: Memproses pengiriman data dengan protokol-protokol, dengan protokol TCP, UDP 
3. **Network**: Layer yang Melakukan Routing data, dengan IP
4. **Link**:  Transferdata antar 2 perakngkat network , dengan Wifi, ethernet, ppp
5. **Physical**: layer yang mengirimkan data secara fisik dalam bentuk bits pada kabel misalnya

data data dikirimkan melalui layer layer tersebut. ketika mengirim dari layer application (yang teratas), data akan melalui protokol-protokol layer selanjutnya agar dapat dikirimkan melalui physical layer (layer terbawah). Ketika mengirim, di setiap layernya data di*enkapsulasi* dengan kode dan di penerimaan, data akan didecode sesuai pemrosesan data tersebut di setiap core-core internet.


Ketika mengirimkan data dari suatu tempat ke tempat lain, pastinya ada delay, delay ini ada karena beberapa hal:
1. **Queueing Delay** : delay yang terjadi ketika router melakukan queueing sebelum diproses.
2. **Processing Delay**: delay yang terjadi ketika router memproses data dengan algoritma routingnya dll.
3. **Transmission Delay**: delay ketika mentransmisikan sejumlah data dengan bandwith tertentu
4. **Propagation Delay**: delay ketika data di distribusikan melalui media secara fisik.



