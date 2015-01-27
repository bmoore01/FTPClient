import socket
import sys
#Used for exit command



def main():

    class fileTransfer:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error, msg:
            print "Failed to create socket, error code : " + str(msg[0]) + " Error message : " + str(msg[1])
        def __init__(self,host,port):
            self.host = host
            self.port = port
        def getConnectionInfo(self):
            print"Please enter the address for the server you're trying to connect to"
            self.host = raw_input(">>")
            print "Now enter the port you want to use(If no port is entered system will default to port 21)"
            self.port = raw_input(">>")
            if len(str(self.port)) == 0:
                self.port = 21

    print "Welcome to FTPy!"
    print 'Would you like to start a file tansfer?y/n :'
    start = raw_input(">>")
    if start[0].lower() == 'y':
        session = fileTransfer(0,0)
        session.getConnectionInfo()
    elif start[0].lower() == 'n':
        print "Closing program"
        sys.exit()





    try:
        remote_ip = socket.gethostbyname( session.host )
    except socket.gaierror:
        #Could not resolve
        print "hostname could not resolve, are you connected to the internet?"
        sys.exit()


    print "You have connected to " + str(session.host) + " the IP is " + str(remote_ip) + " You are connected on port " + str(session.port)



if __name__ == '__main__':
    main()
