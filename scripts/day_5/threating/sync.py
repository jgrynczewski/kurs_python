import time
import threading

x = 128

lock = threading.Lock()


def double():
    global x
    global lock

    lock.acquire()
    while x < 256:
        x *= 2
        print(x)
        time.sleep(1)

    print("Osiągnąłem maksimum")
    lock.release()

def halve():
    global x
    global lock

    lock.acquire()
    while x > 64:
        x /= 2
        print(x)
        time.sleep(1)

    print("Osiągnąłem minimum")
    lock.release()


t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)

t1.start()
t2.start()
