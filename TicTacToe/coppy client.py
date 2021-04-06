#Tic-Tac-Toe over LAN
#player2.py acts as the client
import socket

print '\nWelcome to Tic-Tac-Toe over LAN\nYou are player 2 acting as the client\n\nEnter the private IP address of player 1: '
host=raw_input()

s = socket.socket()
port = 21217

s.connect((host, port))

print s.recv(4096)
playername=raw_input()
s.send(playername)
print '\nWaiting for player 1...'
print s.recv(4096)
while True:
	data=s.recv(4096)
	if 'piece' in data:
		print data
		position=raw_input()
		s.send(position)
	else:
		print data

	if 'Finished' in data:
		break

s.close()