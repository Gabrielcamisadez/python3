import socket
dominio = "dominio.com"
nomes = ["www", "ftp", "mail", "pop", "smtp", "webmail"]

for nome in nomes:
    DNS = nome + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        print(DNS + ": NOt find")

