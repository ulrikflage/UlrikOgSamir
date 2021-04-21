import PySimpleGUI as sg
import socket
from threading import *
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# player = 'O'
enemy_symbol = 'X'
symbol = 'O'


class Client(Thread):
    def __init__(self, sockt):
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

        self.window = sg.Window('TicTacToe Client', layout)

        self.thread = Thread()
        self.sock = sockt
        self.addr = "localhost"
        self.port = 3050
        self.client_data = b''
        self.data = ''
        connected = False
        while not connected:
            try:
                s.connect((self.addr, self.port))
                connected = True
            except ConnectionRefusedError:
                print("Please wait for server to open. Waiting for 5 seconds...")
                sleep(5)
        self.thread.daemon = True
        self.thread.start()
        self.gui()

    def run(self):
        while True:
            # try:
            self.data = self.sock.recv(1024).decode()
            self.sock.send(self.client_data)
            self.client_data = None
        # except OSError:
        #    print('Not Connected. Please wait for server to open. Waiting 5 seconds to retry...')
        #    sleep(5)

    def gui(self):
        global symbol
        global enemy_symbol
        while True:
            event, values = self.window.Read(timeout=20)

            if not len(self.data) < 1:
                self.window.FindElement(self.data).update(enemy_symbol)
            if event == sg.WIN_CLOSED:
                break
            elif event == '1':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'1'
            elif event == '2':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'2'
            elif event == '3':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'3'
            elif event == '4':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'4'
            elif event == '5':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'5'
            elif event == '6':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'6'
            elif event == '7':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'7'
            elif event == '8':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'8'
            elif event == '9':
                self.window.FindElement(event).Update(symbol)
                self.client_data = b'9'
        self.window.close()


Client(s)
