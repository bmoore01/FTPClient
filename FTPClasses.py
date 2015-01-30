import socket
import sys
import base64
import threading
import os
import pickle
#This file will contain all class definitions for the the FTPy progam


#This class contains all the methods needed to make a connection with a server or another client

class fileTrans:
      try:
          sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      except socket.error, msg:
          print "Failed to create socket, error code : " + str(msg[0]) + " Error message : " + str(msg[1])
      def __init__(self,host,port,remote_ip):
          self.host = host
          self.port = port
          self.remote_ip = remote_ip
      def getConnectionInfo(self):
          print"Please enter the address for the server you're trying to connect to"
          self.host = raw_input(">>")
          print "Now enter the port you want to use(If no port is entered system will default to port 21)"
          self.port = raw_input(">>")
          if len(str(self.port)) == 0:
              self.port = 21
          try:
              self.remote_ip = socket.gethostbyname( self.host )
              print self.remote_ip
          except socket.gaierror:
              #Line below for bug fixing
              print "hostname could not resolve"
              sys.exit()
      def connectSocket(self):
          self.sock.connect((self.remote_ip, int(self.port)))
          print "Socket connection successful"



#This class requires the sending file functions

class sendClass(fileTrans):
    def sendFile(self):
        print "What file would you like to send?(Please include the file extention):"
        file_to_send = open(raw_input(">>"),"rt").read()
        encoded_data = base64.b64encode(file_to_send)
        print "Before encoding file was " + str(len(file_to_send))
        try:
            #Attempt to send the file
            self.sock.sendall(encoded_data)
        except socket.error:
            print 'Send failed'
            sys.exit()
        print 'File sent successfully!'
    def threadSend(self):
        t1 = threading.Thread(target=self.sendFile)
        t1.start()
        t1.join()

#This class is used in order to listen for incomming connections

class recvClass(fileTrans):
    def recvFile(self):
        self.sock.bind((self.host,int(self.port)))
        print "Socket binded!"
        self.sock.listen(10)
        print "Socket now listening..."
        while True:
            conn, addr = self.sock.accept()
            print "Recieving file from" + str(addr)
            recieved_file = conn.recv(4096)
            decoded_file = base64.b64decode(recieved_file)
            print decoded_file
            break
