#! /usr/bin/python3

import random 
import socket

serverPort = int(input('Input serverPort: '))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Server is ready.')
while(1):
    rand = random.randint(0, 10)
    message, addr = serverSocket.recvfrom(1024)
    message = message.upper()
    if(rand < 4):
        continue
    serverSocket.sendto(message.encode(), addr)



