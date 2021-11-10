# CNet: A Top-down Approach LAB

My solution of ComputerNetworking: A Top-down Approach Labs and Problems.

The Lectures of CNet please check:

[CNet Lectures](https://github.com/PeterWrighten/ComputerNetworking/blob/main/README.md)

|Lab Note|Solution|
|:--:|:--:|
| WiresharkLAB 0  |  - |
| Socket Prog1  | [A1](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/SocketProgramming/Chapter2)  |
|LAB 1: WebServer|[L1](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/LAB/LAB1_WebServer)|
|LAB 2: UDPPinger|[L2](https://github.com/PeterWrighten/CNet_aTop-downapproach_Lab/tree/main/LAB/LAB2_UDPPinger)|



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