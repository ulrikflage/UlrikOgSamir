# Tic-Tac-Toe over LAN
# player1.py acts as the server
import socket
import random

board = [[' 1 ', ' 2 ', ' 3 '], [' 4 ', ' 5 ', ' 6 '], [' 7 ', ' 8 ', ' 9 ']]
players = []
player1M = []
player2M = []
isFinished = False


def constructBoard():
    s = '\nCurrent Board\n'
    for row in board:
        s += str(row) + '\n'
    s += '\n'
    return s


def printBoard():
    print('\nCurrent Board')
    for row in board:
        print(row)
    print('\n')


def piece(currentPlayer):
    piece = 'Null'
    if currentPlayer == player1:
        piece = ' X '
    else:
        piece = ' O '
    return piece


def checkWinner(board, position, currentPlayer, sock):
    possibilities = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [7, 5, 3]]

    if currentPlayer == player1:
        player1M.append(int(position))
        marks = 0
        for column in possibilities:
            for element in column:
                if element in player1M:
                    marks += 1
                    if marks == 3:
                        print(player1, ' is the winnner!!!\nFinished')

                        sock.send('%s is the winner!!!\nFinished' % player1)
                        return True
            marks = 0
    else:
        player2M.append(int(position))
        marks = 0
        for column in possibilities:
            for element in column:
                if element in player2M:
                    marks += 1
                    if marks == 3:
                        print(player2, ' is the winnner!!!\nFinished')
                        sock.send('%s is the winner!!!\nFinished' % player2)
                        return True
            marks = 0
    if len(player1M) + len(player2M) == 9:
        print('Tied Game!')

        sock.send('Tied Game!')
        return True
    return False


def changePlayer(currentPlayer):
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1
    return currentPlayer


def theGame(location, sock, currentPlayer):
    position = str(location)
    if (int(position) in range(1, 4)):
        try:
            board[0][board[0].index(' %s ' % position)] = piece(currentPlayer)
            printBoard()
            sock.send(constructBoard())
        except:
            if currentPlayer == player2:
                sock.send(
                    '\nError - Reasons:\n1.Position is already taken.\n2. There is a tie\n3.An invalid entry.\n Try '
                    'again')
            else:
                print('\nError - Reasons:\n1.Position is already taked.\n2. There is a tie\n3.An invalid entry.\n Try '
                      'again')

    elif int(position) in range(4, 7):
        try:
            board[1][board[1].index(' %s ' % position)] = piece(currentPlayer)
            printBoard()
            sock.send(constructBoard())
        except:
            if currentPlayer == player2:
                sock.send(
                    '\nError - Reasons:\n1.Position is already taken.\n2. There is a tie\n3.An invalid entry.\n Try '
                    'again')
            else:
                print('\nError - Reasons:\n1.Position is already taked.\n2. There is a tie\n3.An invalid entry.\n Try '
                      'again')

    elif int(position) in range(7, 10):
        try:
            board[2][board[2].index(' %s ' % position)] = piece(currentPlayer)
            printBoard()
            sock.send(constructBoard())
        except:
            if currentPlayer == player2:
                sock.send(
                    '\nError - Reasons:\n1.Position is already taken.\n2. There is a tie\n3.An invalid entry.\n Try '
                    'again')
            else:
                print('\nError - Reasons:\n1.Position is already taked.\n2. There is a tie\n3.An invalid entry.\n Try '
                      'again')

    else:
        if currentPlayer == player2:
            sock.send('Invalid position. Try again')
        else:
            print('Invalid position. Try again')


print('\nWelcome to Tic-Tac-Toe over LAN\nYou are player 1 acting as the server\n\nEnter your private IP address: ')

host = input()

s = socket.socket()
port = 21217
s.bind((host, port))
print('\n\nThis game is running on %s:%s\n\nWaiting for connection...' % (host, port))

s.listen(1)
sock, addr = s.accept()
while True:
    print('Got connection from', addr, '\n\n')

    print('Waiting for player 2...\n')

    a = "Connected to %s\n\nEnter your player name: " % host
    sock.send(bytes(str(a)))
    player2 = sock.recv(4096)
    print('Enter your player name: ')

    player1 = input()
    players.append(str(player1))
    players.append(str(player2))
    play = '\n\nPlayers\n1. %s\n2. %s\n\n%s' % (player1, player2, constructBoard())
    print(play)
    sock.send(bytes(play))
    currentPlayer = random.choice(players)
    while not isFinished:
        if currentPlayer == player1:
            print('\n\nIt is your turn. %s place your piece' % player1)
            sock.send(b"\n\nIt is %s's turn. Please wait..." % player1)
            position = input()
            theGame(position, sock, currentPlayer)
            isFinished = checkWinner(board, position, currentPlayer, sock)
            currentPlayer = changePlayer(currentPlayer)
        else:
            print("\n\nIt is %s's turn. Please wait..." % player2)
            sock.send(b"\n\nIt is your turn. %s place your piece" % player2)
            position = sock.recv(4096)
            theGame(position, sock, currentPlayer)
            isFinished = checkWinner(board, position, currentPlayer, sock)
            currentPlayer = changePlayer(currentPlayer)
    break
sock.close()
