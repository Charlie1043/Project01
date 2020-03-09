from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.1", 8899)

sockfd.bind(server_addr)

while True:
    data, addr = sockfd.recvfrom(1024)
    print("Recv from", addr, "Message:", data.decode())
    sockfd.sendto(b"Thanks", addr)

sockfd.close()