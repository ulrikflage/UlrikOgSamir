import PySimpleGUI as sg
import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 3050
s.bind((HOST, PORT))

koblet_til = False

player = 'O'
symbol = ''

font = 'Helvetica 60'
sg.theme('Default 1')

layout = [
    [sg.Button(size=(3, 1), font=font, key='1', enable_events=True), sg.Button(size=(3, 1), font=font, key='2', enable_events=True),
     sg.Button(size=(3, 1), font=font, key='3', enable_events=True)],
    [sg.Button(size=(3, 1), font=font, key='4', enable_events=True), sg.Button(size=(3, 1), font=font, key='5', enable_events=True),
     sg.Button(size=(3, 1), font=font, key='6', enable_events=True)],
    [sg.Button(size=(3, 1), font=font, key='7', enable_events=True), sg.Button(size=(3, 1), font=font, key='8', enable_events=True),
     sg.Button(size=(3, 1), font=font, key='9', enable_events=True)]
]

window = sg.Window('TicTacToe Client', layout)


class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent: ', self.sock.recv(1024).decode())
            self.sock.send(b'')

    def gui(self):
        global symbol
        while True:
            event, values = window.Read(timeout=20)
            if True:
                symbol = 'X'
            if event == sg.WIN_CLOSED:
                break
            elif event == '1':
                window.FindElement(event).Update(symbol)
                s.send(bytes(event))
            elif event == '2':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '3':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '4':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '5':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '6':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '7':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '8':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
            elif event == '9':
                window.FindElement(event).Update(symbol)
                conn.send(event).encode()
        window.close()





s.listen(5)
print('Server started and listening')
while 1:
    conn, addr = s.accept()
    Client(conn, addr)
