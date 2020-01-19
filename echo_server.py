import socket

ip = '127.0.0.1'
port = 8001
address = (ip, port)
print("Server hosted on", ip + ", listening on port", str(port) + "...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

while(1):
    buf = b''
    connection, addr = s.accept()
    print("Receive data from", addr)
    
    buf = connection.recv(1024)
        
    print(buf.decode())
    connection.send(buf.decode())
    
    connection.close()
s.close()
