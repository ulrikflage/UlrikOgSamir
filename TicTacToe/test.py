import socket  # for sockets
import sys  # for exit
import time  # for sleep

remote_ip = "192.168.100.100"  # should match the instrument’s IP address
port = 5024  # the port number of the instrument service
count = 0


def SocketConnect():
    try:
        # create an AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket.')
        sys.exit()
    try:
        # Connect to remote server
        s.connect((remote_ip, port))
        info = s.recv(4096)
        print(info)
    except socket.error:
        print('failed to connect to ip ' + remote_ip)
    return s


def SocketQuery(Sock, cmd):
    try:
        # Send cmd string
        Sock.sendall(cmd)
        time.sleep(1)
        reply = Sock.recv(4096)
    except socket.error:
        # Send failed
        print('Send failed')
        sys.exit()
    return reply


def SocketClose(Sock):
    # close the socket
    Sock.close()
    time.sleep(.300)


def main():
    global remote_ip
    global port
    global count

    # Body: send the SCPI commands *IDN? 10 times and print the return message
    s = SocketConnect()
    for i in range(10):
        qStr = SocketQuery(s, b'*IDN?')
        print(str(count) + ":: " + str(qStr))
        count = count + 1
        SocketClose(s)
    input('Press "Enter" to exit')


if __name__ == '__main__':
    #main()
    for i in range(1, 4):
        print(i)
