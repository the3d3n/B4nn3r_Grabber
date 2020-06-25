import socket
from IPy import IP


def scan(ip_add):
    converted_ip = check_ip(ip_add)
    print('\n' + '[XD] SCANNING TARGET ' + str(ip_add))
    if flag == 1:
        for port in range(int(port_s), int(port_f) + 1):
            scan_port(ip_add, port)
    elif flag == 0:
        scan_port(ip_add, int(port_s))


def banner_grab(sock):
    return sock.recv(1024)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipadd, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ipadd, port))  # establishing a connection with the given IP address
        try:
            banner = banner_grab(s)
            print('[+] Port ' + str(port) + ' is open: ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is open')
    except:
        pass


if __name__ == '__main__':
    targets = input("[+] Enter target/s to scan(delimit by using a ',' between multiple targets): ")
    port = (input('[+] Enter the range or a singular port number to conduct a scan on(separate by a ","): '))
    if ',' in port:
        port_s, port_f = port.split(',')
        flag = 1
    else:
        port_s = port
        flag = 0
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
