#!/usr/bin/python3

import socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while(1):
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence.decode('utf-8'), addr)
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
