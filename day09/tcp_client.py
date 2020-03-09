

from socket import *

server_addr = ("127.0.0.1",8899)

sockfd = socket()

sockfd.connect(server_addr)
# data = input(">>")
# while data != "##":
while True:
    data = input(">>")
    sockfd.send(data.encode())
    if data == "##" or data == "":
        # data = sockfd.recv(1024)
        # print("From server:", data.decode())
        break
    data = sockfd.recv(1024)
    print("From server:", data.decode())

sockfd.close()

