from tkinter import *
import socket
import threading


def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


HOST = "127.0.0.1"
PORT = 3050
koblet_til = False
conn, addr = None, None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


def motta_data():
    pass


def venter_tilkobling():
    global koblet_til, conn, addr
    conn, addr = s.accept()
    print("Etablert sammenkobling fra client")
    koblet_til = True
    # s.send(b"Velkommen til Tic Tac Toe")
    motta_data()


create_thread(venter_tilkobling)

main = Tk()
main.title("Server side")

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

grid = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8",
]


def click(event):
    shape = choose_shape()
    across = int(c.canvasx(event.x) / 200)
    down = int(c.canvasy(event.y) / 200)
    square = across + (down * 3)

    if grid[square] == "X" or grid[square] == "O":
        return

    if winner():
        return

    if shape == "O":
        c.create_oval(
            across * 200, down * 200,
            (across + 1) * 200, (down + 1) * 200
        )
        grid[square] = "O"
    else:
        c.create_line(
            across * 200, down * 200,
            (across + 1) * 200, (down + 1) * 200
        )
        c.create_line(
            across * 200, (down + 1) * 200,
            (across + 1) * 200, down * 200
        )
        grid[square] = "X"


def choose_shape():
    if grid.count("O") > grid.count("X"):
        return "X"
    else:
        return "O"


def winner():
    for across in range(3):
        row = across * 3
        line = grid[row] + grid[row + 1] + grid[row + 2]
        if line == "XXX" or line == "OOO":
            return True

    for down in range(3):
        line = grid[down] + grid[down + 3] + grid[down + 6]
        if line == "XXX" or line == "OOO":
            return True

    line = grid[0] + grid[4] + grid[8]
    if line == "XXX" or line == "OOO":
        return True

    line = grid[2] + grid[4] + grid[6]
    if line == "XXX" or line == "OOO":
        return True


c.bind("<Button-1>", click)
main.mainloop()
