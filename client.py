import socket
import ssl

protocol = 'https'
header = b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n'
ip = 'www.google.com'

if(protocol == 'https'):
    port = 443
    s = ssl.wrap_socket(socket.socket())
else:
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
address = (ip, port)
s.connect(address)

s.send(header)

buf = b''
while(True):
    info = s.recv(1024)
    if(info):
        buf += info
    else:
        s.close()
        break

if(buf==b''):
    print("Error occurs!\n")
else:
    print(buf)
    
