# Log 5 Jarkomdat

Minggu ini saya belajar tentang TCP generation

ada 4 rule dalam TCP generation:
- RULE 1: receiver akan melakukan ack sesuai dengan sequence selanjutnya dari data yang sudah diterima dari sender setiap 500ms
- RULE 2: Jika dalam 500ms ada 2 atau lebih sequence data yang diterima maka reciever akan mengirim ack kumulatif dari sequence yang terakhir diterima. 
- RULE 3: Jika ada data yang hilang, Receiver akan mengenali ada yang hilang ditengah urutan sequence dan akan terus mengirim ack dari sequence yang hilang walau sender mengirim sequence sequence selanjutnya
- RULE 4: Pada kasus RULE 3 receiver mengirim ack untuk sequence yang hilang maka sender akan kembali mengirim paket data untuk sequence tersebut. dan setelah diterima receiver akan mengirim ack kumulatif dari paket data yang sudah diterima termasuk pada saat ada data yang hilang. 