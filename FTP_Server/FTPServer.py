import socket
import os
import sys
import base64

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



    sys.exit()
if __name__ == '__main__':
    main()
