#This file contains the global variables program needs


'''These two variables allow the program to see if the creation of a class has failed,
the listening boolean is also turned to True if the client is listening
for incomming connections'''
listening = False
create_class_failed = None

sendClientHandlers = []
recvClientHandlers = []
menuExecutionCounter = 0
