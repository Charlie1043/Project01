from threading import Lock, Thread

playing_cards = ""
lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1, 53, 2):
        global playing_cards
        lock1.acquire()
        playing_cards += (str(i) + str(i+1))
        lock2.release()



def print_char():
    for i in range(65, 91):
        global playing_cards
        lock2.acquire()
        playing_cards += chr(i)
        lock1.release()


t1 = Thread(target=print_num)
t2 = Thread(target=print_char)
lock2.acquire()
t1.start()
t2.start()

t1.join()
t2.join()

print(playing_cards)
