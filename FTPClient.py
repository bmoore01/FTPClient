#!/usr/bin/python
from FTPClasses import *
import threading



def menu():
    print 'You can either\n1:Send a file\n2:Recieve a file\n3:look at your transfers\n4:quit'
    start = raw_input(">>")
    i = 0
    while len(start) < 1:
        if i >= 1:
            start = raw_input(">>")
        else:
            print "Input cannot be blank!"
            start = raw_input(">>")
            i += 1
    if int(start) == 1:
        session = sendClass(0,0,0,True)
        session.getConnectionInfo()
        session.connectSocket()
        session.threadSend()
    elif int(start) == 2:
        global create_class_failed
        create_class_failed = False
        r_session = recvClass(0,0,0,False)
        r_session.getConnectionInfo()
        r_session.threadRecv()
        menu()
    elif int(start) == 3:
        print "Threads active: " + str(threading.activeCount())
        print recvClientHandlers
        raw_input("Press return to contiue")
        menu()
    elif int(start) == 4:
        print "Closing progam..."
        sys.exit()
    else:
        print "That's not a valid response please try again"
    print "Operations complete"
    print "Socket connection complete!"

def main():
    print "Welcome to"
    print "_____ _____ ____         _ "
    print "|  ___|_   _|  _ \ _   _| |"
    print "| |_    | | | |_) | | | | |"
    print "|  _|   | | |  __/| |_| |_|"
    print "|_|     |_| |_|    \__, (_)"
    print "                   |___/   "
    clientHandlers =[]
    send_errors = 0
    conn_errors = 0
    menu()


if __name__ == '__main__':
    main()
