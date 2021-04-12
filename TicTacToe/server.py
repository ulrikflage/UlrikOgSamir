import socket
from threading import Thread
from time import sleep

HOST = 'localhost'
PORT = 3050

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

in_values = [' ' for _ in range(9)]
data = [0, 0, 'YourTurn', False]

def create_thread(target):
    thread = Thread(target=target)
    thread.daemon = True
    thread.start()


def receive_data():
    global turn
    global data
    while True:
        data = conn.recv(1024).decode() # receive data from the client, it is a blocking method
        data = data.split('-') # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        x, y = int(data[0]), int(data[1])

        if data[3] == 'False':
            game_over = True


def waiting_for_connection():
    global connection_established, conn, addr
    print('Waiting for client')
    conn, addr = sock.accept()  # wait for a connection, it is a blocking method
    print('client is connected')
    connection_established = True
    receive_data()





def server(socket, host, port):
    global in_values
    global data
    global connection_established
    while True:
        if str(data) == "quit":
            break
        elif len(str(data)) == 2:
            Pos1 = str(data)[0]
            Pos2 = str(data)[1]
            checkPos(Pos1, Pos2)
            # else:
            #    print(data)
            #    in_values.append(str(data))
        conn.sendall(data)
    conn.close()


def board(values):
    underscore_list = ["_" for _ in range(3)]
    underscore = underscore_list[0] + underscore_list[1] + underscore_list[2]

    print("\n")
    print("\t A   B   C")
    print("\t   |   |")
    print("1\t {} | {} | {}".format(values[0], values[1], values[2]))
    print("\t" + underscore + "|" + underscore + "|" + underscore)

    print("\t   |   |")
    print("2\t {} | {} | {}".format(values[3], values[4], values[5]))
    print("\t" + underscore + "|" + underscore + "|" + underscore)

    print("\t   |   |")
    print("3\t {} | {} | {}".format(values[6], values[7], values[8]))
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
    global values
    global in_values
    global data
    global turn
    if checkWin():
        in_values = [' ' for _ in range(9)]
        values = [' ' for _ in range(9)]
    index = int()
    if int(pos2) in range(1, 4) and pos1.lower() in ["a", "b", "c"]:  # check if pos1 is a number
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
                index = 3
            elif index2 == 3:
                index = 6
        elif index1 == 2:
            if index2 == 1:
                index = 1
            elif index2 == 2:
                index = 4
            elif index2 == 3:
                index = 7
        elif index1 == 3:
            if index2 == 1:
                index = 2
            elif index2 == 2:
                index = 5
            elif index2 == 3:
                index = 8
    if data[2] == 'YourTurn':
        turn = True
    if turn:
        if in_values[int(index)] == ' ':
            in_values[int(index)] = "X"
            player = 2
        else:
            print("Not a valid value. Ex. A1\nTry again")
            data = input()
            POS1 = data[0]
            POS2 = data[1]
            checkPos(POS1, POS2)
    else:
        if in_values[int(index)] == ' ':
            in_values[int(index)] = "O"
            player = 1
        else:
            print("Not a valid value. Ex. A1\nTry again")
            data = input()
            POS1 = data[0]
            POS2 = data[1]
            checkPos(POS1, POS2)


def checkWin():
    if values[0] == values[1] == values[2] and values[0] != ' ':
        print(values[0] + " wins")
        return True
    elif values[3] == values[4] == values[5] and values[3] != ' ':
        print(values[3] + " wins")
        return True
    elif values[6] == values[7] == values[8] and values[6] != ' ':
        print(values[6] + " wins")
        return True
    elif values[0] == values[3] == values[6] and values[0] != ' ':
        print(values[0] + " wins")
        return True
    elif values[1] == values[4] == values[7] and values[1] != ' ':
        print(values[1] + " wins")
        return True
    elif values[2] == values[5] == values[8] and values[2] != ' ':
        print(values[2] + " wins")
        return True
    elif values[0] == values[5] == values[8] and values[0] != ' ':
        print(values[0] + " wins")
        return True
    elif values[2] == values[5] == values[6] and values[2] != ' ':
        print(values[2] + " wins")
        return True

    elif values[0] != ' ' and values[1] != ' ' and values[2] != ' ' and values[3] != ' ' and values[4] != ' ' \
            and values[5] != ' ' and values[6] != ' ' and values[7] != ' ' and values[8] != ' ':
        print("Board full. Reseting board.")
        return True
    else:
        return False


# server(SOCKET, HOST, PORT)
def main():
    global player
    global connection_established
    connection_established = False
    player = 1
    create_thread(waiting_for_connection)
    while True:

        if connection_established:
            board(in_values)
            data_in = input()
            POS1 = data_in[0]
            POS2 = data_in[1]
            checkPos(POS1, POS2)
        else:
            print("Waiting for connection. Sleeping for 5 seconds.")
            sleep(5)


values = in_values

main()
