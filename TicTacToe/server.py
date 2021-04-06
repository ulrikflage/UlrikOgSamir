import socket

HOST = '127.0.0.1'
PORT = 3050

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def server(Socket, Host, Port):
    with Socket as s:
        s.bind((Host, Port))
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


server(SOCKET, HOST, PORT)
