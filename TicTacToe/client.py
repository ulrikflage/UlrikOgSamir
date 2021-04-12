import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 3050        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(0, 0, 'YourTurn', False)
    data = s.recv(1024)

print('Received', repr(data))