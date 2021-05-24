#!/usr/bin/python3
import socket
import sys


def  scanHost(ip, startPort, endPort):
	""" Iniciando uma varredura TCP em um determinado endereço IP """

	print('* Iniciando varredura da porta TCP no host% s'% ip)

	# Comece a varredura TCP no host
	tcp_scan(ip, startPort, endPort)

	print('+ Varredura TCP no host% s completa'% ip)

def scanRange(network, startPort, endPort):
    """ Inicia uma varredura TCP em um determinado intervalo de endereços IP """

    print('* Iniciando a varredura da porta TCP na rede %s.0' % network)

    # Repita uma série de endereços IP de host e analise cada destino
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('+ Varredura TCP na rede %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    """ Cria um socket TCP e tenta se conectar através das portas fornecidas """

    for port in range(startPort, endPort + 1):
        try:
            # Create a new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Print if the port is open
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    # Timeout in seconds
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Use: ./portascan.py <IP > <começar porta> <terminar porta>')
        print('Exemplo: ./portascan.py 192.168.1.53 1 65535\n')
        print('Use: ./portascan.py <rede> <começar porta> <terminar porta> -n')
        print('Exemplo: ./portascan.py 192.168.19 1 65535 -n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:
        scanRange(network, startPort, endPort)