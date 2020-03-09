from socket import *

def find_word(word_needed):
    file = open("../day03/dict.txt", "r")
    for line in file:
        word = line.split(" ")[0]
        if word > word_needed:
            file.close()
            return "单词不在词典中"
        elif word == word_needed:
            file.close()
            return line
    else:
        file.close()
        return "单词不在词典中"

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.1", 8888)

sockfd.bind(server_addr)
print("Waiting for connect")

while True:
    data, addr = sockfd.recvfrom(1024)
    print("Recv from", addr, "Message:", data.decode())
    sockfd.sendto(find_word(data.decode()).encode(), addr)

sockfd.close()