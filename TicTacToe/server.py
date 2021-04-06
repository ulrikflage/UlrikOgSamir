import socket

HOST = '192.168.100.100'
PORT = 3050

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def server(Socket, Host, Port):
    with Socket as s:
        s.bind((Host, Port))
        s.listen(5)
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
