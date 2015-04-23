import socket
import sys
import base64
import threading
import os
import time
import config
#This file will contain all class definitions for the the FTPy program
from FTPClient import *

#These two lists will hold the threads which are created
#when the user tells the program to send or recieve a file

kill = None
stop = None


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
      def __init__(self,host,port,remote_ip,sender):
          self.host = host
          self.port = 20
          self.remote_ip = remote_ip
          self.load = loading_screen()
          self.sender = sender
          self.conNum = 1
      def getConnectionInfo(self):
          print"Please enter the address for the server you're trying to connect to"
          self.host = raw_input(">>")
          if self.sender == False:
              usrMultiConn = 'x'
              while usrMultiConn != 'y' and usrMultiConn != 'n':
                  print "Do you want to open more than one connection to this machine?y/n"
                  usrMultiConn = raw_input("->")
                  if usrMultiConn[:1].lower() == 'y':
                      print "How many connections do you want to open to this machine?"
                      usrInputConn = raw_input(">>")
                      while isInt(usrInputConn) == False:
                          print "That's not a number please try again"
                          usrInputConn = raw_input(">>")
                          self.conNum = int(usrInputConn)
          try:
            self.remote_ip = socket.gethostbyname( self.host )
          except socket.gaierror:
            print "hostname could not resolve, make sure you are connected to the internet"
            menu()
      def connectSocket(self):
          try:
              self.sock.connect((self.remote_ip, self.port))
          except:
              print "Error connecting socket"
              menu()
          print "Socket connections successful"



#This class requires the sending file functions

class sendClass(fileTrans):
    def getSendInfo(self):
        print "What file would you like to send?(Please include the file extention):"
        file_to_send = open(raw_input(">>"),"rt").read()
        self.encoded_data = base64.b64encode(file_to_send)
        print "File sent successfully!"
    def sendFile(self):
        print "What file would you like to send?(Please include the file extention):"
        file_name = raw_input(">>")
        file_to_send = open(file_name,"rt").read()
        encoded_data = base64.b64encode(file_to_send)
        package = file_name + ':' + encoded_data
        global kill
        global stop
        kill = False
        stop = False
        self.load.start()
        try:
            #Attempt to send the file
            self.sock.sendall(package)
            time.sleep(1)
            stop = True
        except socket.error or KeyboardInterrupt:
            kill = True
            stop = True
            sys.exit()
    def threadSend(self):
        t1 = threading.Thread(target=self.sendFile)
        global sendClientHandlers
        config.sendClientHandlers.append(t1)
        t1.setDaemon(True)
        t1.start()
        t1.join()
        t1 = None

#This class is used in order to listen for incomming connections

class recvClass(fileTrans):
    def recvFile(self):
        config.listening = True
        tLock.acquire()
        if config.create_class_failed == True:
            menu()
        try:
            self.sock.bind((self.host,self.port))
        except:
            menu()
            global listening
            listening = False
        #print "Socket binded!"
        self.sock.listen(self.conNum)
        #print "Socket now listening..."
        tLock.release()
        conn, addr = self.sock.accept()
        while True:
            part = None
            recieved_package = ""
            while part != '':
                part = conn.recv(1024)
                recieved_package += part
            file_name,recieved_file = recieved_package.split(':')
            file_name = file_name[:len(file_name)]
            decoded_file = base64.b64decode(recieved_file)
            f = open (file_name,"wb")
            f.write(decoded_file)
            f.close()
            break
        config.listening = False
        conn.close()
        self.sock.close()
    def threadRecv(self):
        if config.create_class_failed == True:
            menu()
        else:
            t2 = threading.Thread(target=self.recvFile)
            global recvClientHandlers
            config.recvClientHandlers.append(t2)
            t2.setDaemon(True)
            t2.start()
            t2 = None
            time.sleep(1)

class loading_screen(threading.Thread):
    def run(self):
        global stop
        global kill
        print "Working..."
        sys.stdout.flush()
        i = 0
        while stop != True:
            if (i%4) == 0:
                sys.stdout.write('\b/')
            elif (i%4) == 1:
                sys.stdout.write('\b-')
            elif (i%4) == 2:
                sys.stdout.write('\b\\')
            elif (i%4) == 3:
                sys.stdout.write('\b|')

            sys.stdout.flush()
            time.sleep(0.2)
            i+=1
        if kill == True:
            print '\b\b\b\b Canceled!'
        else:
            print '\b\b Completed!'

#This is just a simple function to check if a string can be converted to an interger
#It is used if the user wants to manually enter a port

def isInt(num):
    try:
        int(num)
        return True
    except:
        return False
