import socket
import ssl

ip = '127.0.0.1'
port = 8002
address = (ip, port)
print("Server hosted on", ip + ", listening on port", str(port) + "...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

while(1):
    
    # Get data from proxy_client.py
    connection, addr = s.accept()
    print("Receive data from", addr)

    proxy_buf = connection.recv(1024)
    
    google_socket = ssl.wrap_socket(socket.socket())
    google_socket.connect(('www.google.com', 443))
    google_socket.send(proxy_buf)
    
    google_buf = b''
    while(True):
        info = google_socket.recv(1024)
        if(info):
            google_buf += info
        else:
            google_socket.close()
            break
    
    connection.send(google_buf)
    connection.close()
s.close()
