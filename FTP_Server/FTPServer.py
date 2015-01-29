import socket
import os
import sys
#Used for decoding
import base64
#Need to save decoded data required for the pickle.dump function
import pickle


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        print addr
        #break
        recieved_file = conn.recv(4096)
        decoded_file = base64.b64decode(recieved_file)
        print decoded_file
        current_dir = os.getcwd()
        print "Current working directory %s" % current_dir
        fileName = "recieved file" + ".txt"
        f = open (fileName,"wb")
        pickle.dump(decoded_file,f)
        f.close()
        break


    sys.exit()
if __name__ == '__main__':
    main()
