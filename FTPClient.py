from FTPClasses import *
import threading



def menu():
    print 'You can either\n1:Send a file\n2:Recieve a file\n3:look at your transfers\n4:quit'
    start = raw_input(">>")
    if int(start) == 1:
        session = sendClass(0,0,0)
        session.getConnectionInfo()
        session.connectSocket()
    elif int(start) == 2:
        r_session = recvClass(0,0,0)
        r_session.getConnectionInfo()
        r_session.recvFile()
        sys.exit()
    else:
        print "That's not a valid response please try again"
    print "Welcome to " + session.host
    print "You have connected to " + str(session.host) + " the IP is " + str(session.remote_ip) + " You are connected on port " + str(session.port)
    print "Socket connection complete!"
    session.threadSend()

def main():
    print "Welcome to"
    print "_____ _____ ____         _ "
    print "|  ___|_   _|  _ \ _   _| |"
    print "| |_    | | | |_) | | | | |"
    print "|  _|   | | |  __/| |_| |_|"
    print "|_|     |_| |_|    \__, (_)"
    print "                   |___/   "

    menu()


if __name__ == '__main__':
    main()
