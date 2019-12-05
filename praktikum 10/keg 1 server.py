import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50004))
s.listen(5)
print"server penjawab otomatis sudah siap"
data =''
kamus = {'nama' : 'Mohammad daffa izzulhaq',
         'NIM':'L200190204',
         'angkatan': '19',}
while data.lower() != 'keluar':
    komm,addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print 'perintah',data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf,perintah tidak dimengerti')
