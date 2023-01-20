import time

quit = False

def worker():
    counter = 0
    while quit == False:
        counter += 1
        time.sleep(1)
        print(counter)


worker()

input("Naciśnij enter, żeby przerwać: ")
quit = True
