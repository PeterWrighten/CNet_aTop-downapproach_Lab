import socket
import time


serverPort = input('Input your port number: ')
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1.0)
i = 0
while(1):
    start = time.time()
    message = ('Ping %d StartTime: %s ' % (i+1, start))

    try:    
        clientSocket.sendto(message.encode(), ('', serverPort))
        modifiedMessage, addr = clientSocket.recvfrom(1024)
        RTT = time.time() - start
        print(modifiedMessage.decode() + ('RTT: %.3f' % RTT))

    except Exception as e:# TimeoutError is belonged to Exception obj
        print('Request timed out')
    i += 1

clientSocket.close()



