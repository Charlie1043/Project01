from socket import *
import struct

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

server_addr = ("127.0.0.1", 9999)

sockfd.bind(server_addr)

f = open("student.txt", "a")
st = struct.Struct("i12sif")

while True:
    data, addr = sockfd.recvfrom(1024)
    line = st.unpack(data)
    if line[0] == "".encode():
        break
    print("Recv from:", addr, "Data:", data)
    if line[-1] >= 90:
        line = list(line)
        line[1] = line[1].strip(b"\x00").decode()
        f.writelines(str(line)+"\n")
        f.flush()
        sockfd.sendto((line[1]+"的成绩被写入").encode(), addr)
    else:
        sockfd.sendto(b"Thanks", addr)


f.close()
sockfd.close()


