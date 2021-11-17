# CNet: A Top-down Approach LAB

My solution of ComputerNetworking: A Top-down Approach Labs and Problems.


The Lectures of CNet please check:

講義のノートはこちらに取ります：

[CNet Lectures](https://github.com/PeterWrighten/ComputerNetworking/blob/main/README.md)

|Lab　|Solution|問題文の日本語翻訳|
|:--:|:--:|:--:|
| WiresharkLAB 0  |  - |-|
| Socket Prog1  | [A1](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/SocketProgramming/Chapter2)  |[TCP/UDP Socket]()|
|LAB 1: WebServer|[L1](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/LAB/LAB1_WebServer)|[ウェブサーバ]()|
|LAB 2: UDPPinger|[L2](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/LAB/LAB2_UDPPinger)|[UDP Pinger]()|
|LAB 3: SMTP|[L3](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/LAB/LAB3_SMTP)|[メールサーバ]()|



# Notes

## WiresharkLAB0

>Actually, this lab is from CS144.

DEMO: Wireshark

Wireshark is an application that lets you actually observe the datagrams being sent and received on your machine over the Internet.

We filtered for packets with a particular IP address (given by Keith):

![demo](/WiresharkLAB/LAB0/demo.png)

Image: screenshot of Wireshark filter box, with `ip.dst == 171.64.65.14` filter applied. This filters for IP packets with destination IP address 171.64.65.14.

We then pinged that IP address from a terminal window

```$ ping 171.64.65.14```

**APPENDIX:Wireshark**

>A Network Packet Analyzer

>You could filter the particular IP dst to examine its packet info.

## Socket Programming: Creating Network Applications

* Implementation: Conform Protocol Standard
* Proprietary APP: Choose Port

> ```127.0.0.1``` is local hostname.

### Socket Programming with UDP
Unreliable; Datagram


### Socket Programming with TCP

Coneection-oriented; Reliable


### Lab 1: WebServer

>Based on TCP Protocol

>Modular: Socket, Sys

**Function:**

- ```socket.socket(socket.AF_INET, socket.SOCK_STREAM)```: Initialization

- ```socket.bind((serverAdress, serverPort))```: Bind socket (Usually Used For Server)

- ```socket.recv(buffer size)```: Receive obj

- ```socket.recvfrom(buffersize, (serverAddress, serverPort))```: Receive obj from server

- 
