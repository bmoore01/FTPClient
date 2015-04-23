import socket
import sys

def main():
    print "Welcome to pyChat, if it doesn't work use sudo"
    print "1: Start \n 2:Close"
    start = raw_input('>')
    if int(start) == 1:
        chatWindow = chatter('',0,0)
        chatWindow.getUsrInfo()
        chatWindow.getSvrInfo()
        chatWindow.clientChat()
    if int(start) == 2:
        print "Closing program"
        sys.exit()
    else:
        print "command not recognised"
        main()

class chatter:
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
        print "Socket creaton failed"
    def __init__(self,usr,svrAddr,port):
        self.usr = usr
        self.svrAddr = svrAddr
        self.port = port
    def getUsrInfo(self):
        print "Enter a username:"
        usr = raw_input('<')
        usr = '<' + usr + '>'
    def getSvrInfo(self):
        print "Enter IP of your room server:"
        self.svrAddr = raw_input('/')
        self.port = 18
    def clientChat(self):
        try:
            self.sock.connect((self.svrAddr,self.port))
        except:
            print "Cannot connect to the server."
            main()
        msg = ''
        while msg != 'q':
            msg = raw_input('>')
            package = self.usr + ':' + msg
            self.sock.sendall(package)
            recvData = self.sock.recv(1024)
            rUsr, rMsg = recvData.split(':')
            print rUsr + " >> " + rMsg
        print "exiting room"
        main()


if __name__ == '__main__':
    main()
