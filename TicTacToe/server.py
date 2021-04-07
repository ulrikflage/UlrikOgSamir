import socket

HOST = '172.18.170.214'
PORT = 3050

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


in_values = [' ' for _ in range(9)]


def server(socket, host, port):
    global in_values
    with socket as s:
        s.bind((host, port))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if str(data) == "quit":
                    break
                elif len(str(data)) == 2:
                    Pos1 = str(data)[0]
                    Pos2 = str(data)[1]
                    checkPos(Pos1, Pos2)
                #else:
                #    print(data)
                #    in_values.append(str(data))
                conn.sendall(data)
            conn.close()


def board(values):
    underscore_list = ["_" for _ in range(3)]
    underscore = underscore_list[0] + underscore_list[1] + underscore_list[2]

    print("\n")
    print("\t   |   |")
    print("\t {} | {} | {}".format(values[0], values[1], values[2]))
    print("\t" + underscore + "|" + underscore + "|" + underscore)

    print("\t   |   |")
    print("\t {} | {} | {}".format(values[3], values[4], values[5]))
    print("\t" + underscore + "|" + underscore + "|" + underscore)

    print("\t   |   |")
    print("\t {} | {} | {}".format(values[6], values[7], values[8]))
    print("\t   |   |")
    print("\n")


def checkPos(pos1, pos2):
    """
    Translate position to index of values list
    :param pos1:
    :param pos2:
    :return:
    """
    global player
    index = int()
    if int(pos2) in range(1, 4) and pos1.lower() in ["a", "b", "c"]: # check if pos1 is a number
        if pos1.lower() == "a":
            index1 = 1
        elif pos1.lower() == "b":
            index1 = 2
        elif pos1.lower() == "c":
            index1 = 3

        if pos2.lower() == "1":
            index2 = 1
        elif pos2.lower() == "2":
            index2 = 2
        elif pos2.lower() == "3":
            index2 = 3

        if index1 == 1:
            if index2 == 1:
                index = 0
            elif index2 == 2:
                index = 1
            elif index2 == 3:
                index = 2
        elif index1 == 2:
            if index2 == 1:
                index = 3
            elif index2 == 2:
                index = 4
            elif index2 == 3:
                index = 5
        elif index1 == 3:
            if index2 == 1:
                index = 6
            elif index2 == 2:
                index = 7
            elif index2 == 3:
                index = 8

    if player == 1:
        in_values[int(index)] = "X"
        player = 2
    else:
        in_values[int(index)] = "O"
        player = 1


#server(SOCKET, HOST, PORT)
def main():
    global player
    player = 1
    while True:
        board(in_values)
        data = input()
        POS1 = data[0]
        POS2 = data[1]
        checkPos(POS1, POS2)
#values=in_values

main()
