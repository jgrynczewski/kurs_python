import time
import threading

quit = False


def worker(name):
    counter = 0
    while quit == False:
        counter += 1
        time.sleep(1)
        print(f"{name}: {counter}")


# Utworzenie wątku
thread_1 = threading.Thread(
    target=worker,
    daemon=True,
    args=("Goffer 1", )
)
thread_2 = threading.Thread(
    target=worker,
    daemon=True,
    args=("Goffer 2", )
)


# Wystartowanie wątku
thread_1.start()
time.sleep(0.4)
thread_2.start()

input("Naciśnij enter, żeby przerwać: ")
quit = True
