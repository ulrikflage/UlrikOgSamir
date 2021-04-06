import socket

HOST = '172.18.170.214'
PORT = 3050

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with SOCKET as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(data)
            conn.sendall(data)

