from threading import Thread, Lock
from socket import *

HOST = "0.0.0.0"
PORT = 8899
ADDR = (HOST, PORT)


s_listen = socket()
s_listen.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

s_listen.bind(ADDR)
s_listen.listen(3)


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
    t = Thread(target=handle, args=(conn,))
    # t.daemon
    t.start()
    t.join()
