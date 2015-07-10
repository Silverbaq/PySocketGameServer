__author__ = 'silverbaq'

#!/usr/bin/python
from socket import *
from thread import *
from SocketGames import *

# Defining server address and port
host = 'localhost'
port = 52000

sock = socket()
sock.bind((host, port))
#Listening at the address
sock.listen(5) #5 denotes the number of clients can queue


def clientthread(conn):
    conn.send('Hi! I am server\n') #send only takes string

    active = True

    # Shows game menu
    sg = SocketGames()
    conn.send(sg.getGameMenu())

    # Sets game to play
    gameset = False
    while not gameset:
        data = conn.recv(1024) # 1024 stands for bytes of data to be received

        value = sg.choiceGame(int(data))
        if isinstance(value, basestring):
            conn.send(value)
        else:
            game = value
            gameset = True

    conn.send("Guess a number between 1 - 100\r\n")

    while active:
        # Receiving from client
        data = conn.recv(1024) # 1024 stands for bytes of data to be received

        try:
            if data == "Exit\r\n":
                # Stops client
                active = False
            elif data == "Restart\r\n":
                # Restart game
                conn.send(game.newGame())
            else:
                # Guesses - and returns result to client
                conn.send(game.guess(int(data)))
        except Exception as ex:
            print ex.message
            continue

    # closes connection
    conn.close()
    print 'Client left'

serverrunning = True

while serverrunning:

    try:
        # Accepting incoming connections
        conn, addr = sock.accept()

        # Creating new thread. Calling clientthread function for this function and passing conn as argument.
        start_new_thread(clientthread,(conn,)) # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    except KeyboardInterrupt:
        serverrunning = False

print "Socket Shutdown"
sock.close()



