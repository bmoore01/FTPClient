from FTPClasses import *
import threading


def menu():
    print 'You can either\n1:Send a file\n2:Recieve a file\n3:look at your transfers\n4:quit\n'
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
        s_session = sendClass(0,0,0,"")
        try:
            s_session.getConnectionInfo()
        except:
            print "error with file name"
        s_session.connectSocket()
        print "Welcome to " + s_session.host
        s_session.getSendInfo()
        s_session.threadSend()
        menu()
    elif int(start) == 2:
        r_session = recvClass(0,0,0,"")
        r_session.getConnectionInfo()
        r_session.threadRecv()
        menu()
    elif int(start) == 4:
        print "Exiting program"
        sys.exit()
    else:
        print "That's not a valid response please try again"
    print "Operations complete"

def main():
    print "Welcome to"
    print " _____ _____ ____        _ "
    print "|  ___|_   _|  _ \ _   _| |"
    print "| |_    | | | |_) | | | | |"
    print "|  _|   | | |  __/| |_| |_|"
    print "|_|     |_| |_|    \__, (_)"
    print "                   |___/   "

    menu()


if __name__ == '__main__':
    main()
