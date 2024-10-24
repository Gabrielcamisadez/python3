import socket
from concurrent.futures import ThreadPoolExecutor

def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    try:
        s.connect((host, port))
        return f'Port {port} is open!'
    except:
        return f'Port {port} is closed!'
    finally:
        s.close()

def main():
    host = str(input('HOST: '))
    inicial_port = int(input('PORTA INICIAL: '))
    final_port = int(input('PORTA FINAL: ')) 

    try:
        ip = socket.gethostbyname(host)
        print(f'Iniciando o scan em {ip} \n')
    except:
        print('HOST-ERROR')
        return

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [
            executor.submit(scan, ip, inicial_port, final_port) for port in range(inicial_port, final_port + 1)
        ] 

        for future in futures:
            print(future.result())

if __name__ == '__main__':
    main()                 