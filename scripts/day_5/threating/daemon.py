import time
import threading

quit = False


def worker():
    counter = 0
    while quit == False:
        counter += 1
        time.sleep(1)
        print(counter)


# Utworzenie wątku
thread_1 = threading.Thread(target=worker, daemon=True)
# Wystartowanie wątku
thread_1.start()


input("Naciśnij enter, żeby przerwać: ")
quit = True
