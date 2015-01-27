import socket
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(10)

    while True:
        sc, address = s.accept()
        print address






if __name__ == '__main__':
    main()
