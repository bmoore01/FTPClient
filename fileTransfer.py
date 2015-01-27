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
