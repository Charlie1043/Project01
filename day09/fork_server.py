"""
    基于fork的多进程并发
"""

from socket import *
import os
import signal

HOST = ("0.0.0.0")
PORT = 8888
ADDR = (HOST, PORT)

s_listen = socket()
s_listen.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s_listen.bind(ADDR)
s_listen.listen(3)

print("Listen the port 8888")
signal.signal(signal.SIGCHLD, signal.SIG_IGN) #处理僵尸进程

# 处理客户端的请求
def handle(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(data)
        conn.send(b"OK")
    conn.close()


while True:
    conn, addr = s_listen.accept()
    print("Connect from", addr)

    # 创建一个新的进程处理客户端请求（以把父进程解放出来）
    pid = os.fork()
    if pid == 0:
        # 处理客户端请求
        handle(conn)
        os._exit(0) # 子进程处理完客户端请求后就退出
    else:
        # 出错或者（父进程，原有进程）继续等待客户端连接
        continue


s_listen.close()




