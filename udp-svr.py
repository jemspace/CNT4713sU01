# Chepurna
# ID:6152714
# CNT4713-U01
# 1/19/2020

import socket

localIP = "127.0.0.1"
localPort = 12200
bufferSize = 1024

msg = "hello UDP"
bytesToSend = str.encode(msg)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server listens")

flag = 0
while flag == 0:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    c_msg = "Incoming message: {}".format(message)
    c_IP = "Client address: {}".format(address)
    print(c_msg + " --- " + c_IP)
    if "-/E" in c_msg: flag = 1

