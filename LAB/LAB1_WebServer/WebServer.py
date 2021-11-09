#!/usr/bin/python3

import socket
import sys

serverPort = int(input('Input port number: '))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while(1):
    print('Ready to serve...')
    connectionSocket, serveraddr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = ' HTTP/1.1 200 OK\nConnection: close\nCotent-type: text/html\nContent-length: %d\n\n'%(len(outputdata))
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    
    except IOError:
        Error = 'HTTP/1.1 404 NotFound\n\n'
        connectionSocket.send(Error.encode())
        connectionSocket.close()
    serverSocket.close()
        



