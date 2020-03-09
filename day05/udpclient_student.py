import struct
from socket import *

server_addr = ("127.0.0.1", 9999)

sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    id = input("请输入学生id：")
    if id == "":
        break
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    score = input("请输入学生分数：")
    st = struct.Struct("i12sif")
    data = st.pack(int(id), name.encode(), int(age), float(score))
    sockfd.sendto(data, server_addr)
    print("已发送一条学生成绩")
    data, addr = sockfd.recvfrom(1024)
    print("Recv %s from %s" % (data.decode(), addr))

sockfd.close()