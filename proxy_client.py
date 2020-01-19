import socket
import ssl

header = b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n'
ip = '127.0.0.1'

port = 8002
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
    
