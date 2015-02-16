import socket
import os
import sys
import base64

HOST = ''
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, 8080))
        print "Bind sucessful"
    except socket.error , msg:
        print 'Bind failed'
        sys.exit()
    print "Socket bind complete"

    s.listen(10)
    print "Socket now listening"

    conn, addr = s.accept()
    print address
    #break
    recieved_file = conn.recv(4096)
    decoded_file = base64.b64decode(recieved_file)
    print decoded_file



    sys.exit()
if __name__ == '__main__':
    main()
