from socket import *

server_addr = ("127.0.0.1", 8899)

sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input(">>")
    if not data:
        break
    sockfd.sendto(data.encode(), server_addr)
    data, addr = sockfd.recvfrom(1024)
    print("服务端：", data.decode())

sockfd.close()

