import socket

HOST = '192.168.0.100'
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

def board():
    """
       |   |
       |   |
    ___|___|___
       |   |
       |   |
    ___|___|___
       |   |
       |   |
       |   |
    """
    string = ""
    for i in range(9):

        for j in range(9):
            if j == 4 or j == 7:
                string += "|"
            elif i == 2 or i == 5:
                if j < 3:
                    string += "_"
                elif 4 < j:
                    string += "__"
                elif j < 7:
                    string += "_"
                elif j > 7:
                    string += "_"
            elif j < 4:
                string += " "
            elif j > 4:
                string += "  "
            elif j > 7:
                string += "   "
        string += "\n"
    print(string)

board()
#server(SOCKET, HOST, PORT)
