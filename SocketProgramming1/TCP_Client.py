#! /usr/bin/python3


import socket


serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode('utf-8'))
clientSocket.close()
