import socket
import sys
import base64
import threading
import os
import time
from FTPClient import *
#This file will contain all class definitions for the the FTPy progam
sendClientHandlers = []
recvClientHandlers = []

'''These three variables count the connection, recieve and send errors the program
comes across so they can provide information to the user that the sends have failed since
they will be running in threads and printing to the screen in multiple threads causes all
sorts of problems'''

tLock = threading.Lock()
#This class contains all the methods needed to make a connection with a server or another client

class fileTrans:
      try:
          sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      except socket.error, msg:
          print "Failed to create sockets, error code : " + str(msg[0]) + " Error message : " + str(msg[1])
      def __init__(self,host,port,remote_ip):
          self.host = host
          self.port = port
          self.remote_ip = remote_ip
      def getConnectionInfo(self):
          print"Please enter the address for the server you're trying to connect to"
          self.host = raw_input(">>")
          #If statement used just for making testing easier
          if len(str(self.host)) == 0:
              self.host = "127.0.0.1"
          print "Now enter the port you want to use(If no port is entered system will default to port 8080)"
          self.port = raw_input(">>")
          if len(str(self.port)) == 0:
              self.port = "8080"
          try:
              self.remote_ip = socket.gethostbyname( self.host )
              print self.remote_ip
          except socket.gaierror:
              #Line below for bug fixing
              print "hostname could not resolve, make sure you are connected to the internet"
              conn_errors += 1
              menu()
      def connectSocket(self):
          try:
              self.sock.connect((self.remote_ip, int(self.port)))
          except:
              print "Error connecting socket"
              #conn_errors += 1
              #menu()
          print "Socket connections successful"



#This class requires the sending file functions

class sendClass(fileTrans):
    def getSendInfo(self):
        print "Lock acquired"
        print "What file would you like to send?(Please include the file extention):"
        file_to_send = open(raw_input(">>"),"rt").read()
        self.encoded_data = base64.b64encode(file_to_send)
        print "File sent successfully!"
    def sendFile(self):
        print "What file would you like to send?(Please include the file extention):"
        file_to_send = open(raw_input(">>"),"rt").read()
        encoded_data = base64.b64encode(file_to_send)
        try:
            #Attempt to send the file
            self.sock.sendall(encoded_data)
        except socket.error:
            #This error counter will be used down the line to display errors in the 'view your transfers' menu
            #send_errors += 1
            sys.exit()
        #tLock.release()
        print 'File sent successfully!'
    def threadSend(self):
        t1 = threading.Thread(target=self.sendFile)
        global sendClientHandlers
        sendClientHandlers.append(t1)
        t1.setDaemon(True)
        t1.start()
        t1.join()
        t1 = None

#This class is used in order to listen for incomming connections

class recvClass(fileTrans):
    def recvFile(self):
        tLock.acquire()
        self.sock.bind((self.host,int(self.port)))
        #print "Socket binded!"
        self.sock.listen(10)
        #print "Socket now listening..."
        tLock.release()
        conn, addr = self.sock.accept()
        while True:
            #print "Recieving file from" + str(addr)
            part = None
            recieved_file = ""
            while part != '':
                part = conn.recv(1024)
                recieved_file += part
            decoded_file = base64.b64decode(recieved_file)
            current_dir = os.getcwd()
            #print "Current working directory %s" % current_dir
            fileName = "recieved file" + ".jpg"
            f = open (fileName,"wb")
            f.write(decoded_file)
            f.close()
            break
        conn.close()
        self.sock.close()
    def threadRecv(self):
        t2 = threading.Thread(target=self.recvFile)
        global recvClientHandlers
        recvClientHandlers.append(t2)
        t2.setDaemon(True)
        t2.start()
        t2 = None
        time.sleep(1)
