import socket
dominio = "http://sigapep.saude.prefeitura.sp.gov.br"
nomes = ["ns1", "www", "ftp", "mail", "pop", "smtp", "webmail", "ns2", "ns3"]

for nome in nomes:
    DNS = nome + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        print(DNS + ": NOt find")

