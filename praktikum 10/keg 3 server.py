import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "Server Siap"
perintah = ""
si=0

while perintah != "keluar":
    komm, addr = s.accept()
    while perintah != "keluar":
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == "keluar":
            komm.send("done")
            s.close()
            break
        print "pesan: ", perintah
        if len(item)==2:
            if perintah == "sisi":
                si=int(item[1])
                komm.send("sisi disimpan")
            else:
                komm.send("Pesan tidak diketahui")
        elif perintah == "hitung":
            L=float(si*si)
            response = "Luas persegi dengan sisi {} adalah {}".format(si,L)
            komm.send(response)
        else:
            komm.send("Pesan tidak diketahui")
