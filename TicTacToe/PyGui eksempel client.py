import PySimpleGUI as sg
import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 3050
s.bind((HOST, PORT))

koblet_til = False

#player = 'O'
enemy_symbol = 'X'
symbol = 'O'

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
        self.client_data = b''
        self.data = ''
        self.start()

    def run(self):
        self.gui()
        while 1:
            self.data = self.sock.recv(1024).decode()
            self.sock.send(self.client_data)
            self.client_data = None

    def gui(self):
        global symbol
        global enemy_symbol
        while True:
            event, values = window.Read(timeout=20)

            if self.data:
                window.FindElement(self.data).update(enemy_symbol)
            if event == sg.WIN_CLOSED:
                break
            elif event == '1':
                window.FindElement(event).Update(symbol)
                self.client_data = b'1'
            elif event == '2':
                window.FindElement(event).Update(symbol)
                self.client_data = b'2'
            elif event == '3':
                window.FindElement(event).Update(symbol)
                self.client_data = b'3'
            elif event == '4':
                window.FindElement(event).Update(symbol)
                self.client_data = b'4'
            elif event == '5':
                window.FindElement(event).Update(symbol)
                self.client_data = b'5'
            elif event == '6':
                window.FindElement(event).Update(symbol)
                self.client_data = b'6'
            elif event == '7':
                window.FindElement(event).Update(symbol)
                self.client_data = b'7'
            elif event == '8':
                window.FindElement(event).Update(symbol)
                self.client_data = b'8'
            elif event == '9':
                window.FindElement(event).Update(symbol)
                self.client_data = b'9'
        window.close()
