#! /usr/bin/python3

import socket

msg = "\r\n I love computer networks!"

endmsg = "\r\n. \r\n"

mailserver = "smtp.gmail.com"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 25))
