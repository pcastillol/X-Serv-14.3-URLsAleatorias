#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
    while True:
        numRandom = str(random.randint(0,999999999))
        url = "http://localhost:1234/" + numRandom

        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(1024))
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body>Hola. "
                        "<a href=" + url + ">Dame otra.</a>" +
                        "\r\n" +
                        "</body></html>","utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    print("\nClosing binded socket")
    mySocket.close()
