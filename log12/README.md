# Jarkomdat week 12

## Wireless Network
wireless network adalah jaringan yang terhubung tanpa kable / wireless. di wireless network, host pada jaringan tidak menentu keberadaan koneksi nya dengan jaringan, maka itu salah satu sifat wireless network adalah dapat menghandle mobility.

### Elements of Wireless Network
- **Wireless Host**, host yang terkoneksi dengan wireless
- **Base Station**, terkoneksi dengan wired network, bertugas mengirimkan paket antar wired dan wireless network.
- **Wireless Link**, penyambung antar host dengan base station. link yang tidak terlihat secara fisiknya karena menggunakan gelombang sinyal wireless. memiliki beragam data rates dan transmission distance (4G, 3G, 2G)
- **Infrastructure mode**, host terhubung dengan base station. pada mobile host basestation yang terhubung akan berubah ubah karena. perangkat bergerak. 
- **Ad Hoc mode**, tidak memiliki base station, hanya mengandalkan setiap node host yang mengorganize diri mereka sendiri terhubung ke network. 


### wireless link characteristics
- decreased signal strength
- interference from other sources
- multipath propagation
- SNR: signal-to-noise ratio
- SNR versus BER tradeoffs
- hidden terminal problems
- Signal attenuation


### IEEE 802.11
protokol yang umum digunakan untuk wireless network LAN adalah IEEE 802.11\
protokol ini sendiri dibagi dengan beberapa tiipe yang berbeda (a, b, g,n ) dengan range dan kecepatan yang berbeda beda dan semuanya menggunakan CSMA/CD untuk multiple access agar meminimalisir collision. 

di dalam protokol ini biasanya dibagi kedalam 11 - 14 channel tergantung tipe protokol. channel ini digunakan untuk membagi koneksi agar meminimalisir overlapping antar wireless yang berbeda.

agar host dapat terkoneksi dengan access point tertentu, maka dilakukan scanning. ada 2 jenis scanning yaitu passive scanning dan active scanning. jika passive yang mengirim request addalah access pointnya dulu, sebaliknya active scanning host yang akan mnegirimkan request broadcast frame. 



