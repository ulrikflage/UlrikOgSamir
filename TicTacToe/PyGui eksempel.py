import PySimpleGUI as sg
import socket

HOST = 'localhost'
PORT = 3050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sg.theme('Default 1')

layout = [
    [sg.Button(size=(20, 10), key='1', enable_events=True), sg.Button(size=(20, 10), key='2', enable_events=True),
     sg.Button(size=(20, 10), key='3', enable_events=True)],
    [sg.Button(size=(20, 10), key='4', enable_events=True), sg.Button(size=(20, 10), key='5', enable_events=True),
     sg.Button(size=(20, 10), key='6', enable_events=True)],
    [sg.Button(size=(20, 10), key='7', enable_events=True), sg.Button(size=(20, 10), key='8', enable_events=True),
     sg.Button(size=(20, 10), key='9', enable_events=True)]
]

window = sg.Window('TicTacToe', layout)


def connect():
    s.connect((HOST, PORT))
    s.listen(1)


def GUI():
    connect()
    while True:
        event, values = window.Read(timeout=20)
        if event == sg.WIN_CLOSED:
            break
        elif event == '1':
            print('1')
        elif event == '2':
            print('2')

GUI()
