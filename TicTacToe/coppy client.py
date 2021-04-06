# Tic-Tac-Toe over LAN
# player2.py acts as the client
import socket

print('\nWelcome to Tic-Tac-Toe over LAN\nYou are player 2 acting as the client\n\nEnter the private IP address of '
      'player 1: ')
host = input()

s = socket.socket()
port = 21217

s.connect((host, port))

print(s.recv(4096))
playername = input()
s.send(bytes(playername))
print('\nWaiting for player 1...')
print(s.recv(4096))
while True:
    data = s.recv(4096)
    if b'piece' in data:
        print(data)
        position = input()
        s.send(bytes(position))
    else:
        print(data.decode())

    if b'Finished' in data:
        break

s.close()
