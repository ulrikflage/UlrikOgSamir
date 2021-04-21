import PySimpleGUI as sg
import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize socket as 's'
HOST = 'localhost'  # socket.gethostname()                                  # uses this ip address for bind
PORT = 3050  # uses this port for bind
s.bind((HOST, PORT))  # binds socket to an ip address
s.listen(1)

enemy_symbol = 'O'
symbol = 'X'


class Client(Thread):
    def __init__(self):  # runs first when class is called
        font = 'Helvetica 60'  # sets the font of the symbols on buttons to Helvetica with size 60
        sg.theme('Default 1')  # uses the theme 'Default 1' for the window
        self.layout = [  # grid of buttons for tic tac toe
            [sg.Button(size=(3, 1), font=font, key='1', enable_events=True), sg.Button(size=(3, 1), font=font, key='2', enable_events=True),
             sg.Button(size=(3, 1), font=font, key='3', enable_events=True)],
            [sg.Button(size=(3, 1), font=font, key='4', enable_events=True), sg.Button(size=(3, 1), font=font, key='5', enable_events=True),
             sg.Button(size=(3, 1), font=font, key='6', enable_events=True)],
            [sg.Button(size=(3, 1), font=font, key='7', enable_events=True), sg.Button(size=(3, 1), font=font, key='8', enable_events=True),
             sg.Button(size=(3, 1), font=font, key='9', enable_events=True)]
        ]

        self.window = sg.Window('TicTacToe Server', self.layout)  # sets window object to a variable
        Thread.__init__(self)  # runs init code of Thread object

        # listens for connections (client)
        print('Server started and listening')  # prints out message that connection is listened for
        self.conn, self.addr = s.accept()  # waiting for connection, blocking code
        self.koblet_til = True  # sets variable 'koblet_til' to True after connection is established
        # client_ip, client_port = s.getpeername()                            # gets ip address and port of client
        # print("\nConnected to {} on port {}".format(client_ip, client_port))# prints ip and port of client
        print('Tried to connect')
        self.client_data = bytes()  # initializes variable 'client_data' as type bytes
        self.data = str()  # initializes variable 'client_data' as type string
        self.daemon = True  # sets thread to use daemon
        self.start()  # starts thread code
        self.gui()  # starts GUI code

    def run(self):
        while True:  # repeat
            pass
            # self.recieve_data()                                           # runs the function 'recieve_data' in separate thread

    def recieve_data(self):
        while True:  # repeat until
            if self.koblet_til:  # checks if connection was successful
                self.data = self.conn.recv(1024).decode()  # recieves data from opponent and saves it in the 'data' variable
                if self.client_data is not None:  # checks if client_data has a valid
                    self.conn.send(bytes(self.client_data))  # sends player's data to
                    self.client_data = None  # resets variable 'client_data' so that we will not send this data multiple times
                if not len(self.data) < 1:  # checks if data is actually recieved
                    break  # breaks the loop to continue GUI code

    def gui(self):
        global symbol
        global enemy_symbol
        while True:
            self.recieve_data()  # run the function named 'recieve_data', this is a blocking code
            event, values = self.window.Read(timeout=20)  # gets events and values from elements in the GUI
            # also updating GUI every 20 ms

            if not len(self.data) < 1:  # checks if the data is not empty
                self.window.FindElement(self.data).update(enemy_symbol)  # draws opponent's symbol on the correct square in the grid
            if event == sg.WIN_CLOSED:  # checks if the player closes the window
                break  # exit while loop
            elif event == '1':  # checks if square with key '1' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'1'  # saves the key of the element in a variable to be sent to opponent
            elif event == '2':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'2'  # saves the key of the element in a variable to be sent to opponent
            elif event == '3':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'3'  # saves the key of the element in a variable to be sent to opponent
            elif event == '4':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'4'  # saves the key of the element in a variable to be sent to opponent
            elif event == '5':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'5'  # saves the key of the element in a variable to be sent to opponent
            elif event == '6':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'6'  # saves the key of the element in a variable to be sent to opponent
            elif event == '7':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'7'  # saves the key of the element in a variable to be sent to opponent
            elif event == '8':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'8'  # saves the key of the element in a variable to be sent to opponent
            elif event == '9':  # checks if square with key '2' is pressed
                self.window.FindElement(event).Update(symbol)  # draws player's symbol on the square that was clicked
                self.client_data = b'9'  # saves the key of the element in a variable to be sent to opponent
        self.window.close()  # closes the window object after player has closed the window
        s.close()  # closes connection between server and client


a = Client()  # starts the class 'Client'
