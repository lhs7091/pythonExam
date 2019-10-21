import threading
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "~~~~~~~~~~", time.time())

def print_cube(num):
    print("Cube = {}".format(num*num*num))

def print_sqare(num):
    print("Sqare = {}".format(num * num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(2, ))
    t2 = threading.Thread(target=print_sqare, args=(2, ))

    t1.start() # start of instance
    t2.start()

    t1.join() # wait until this instance is terminated
    t2.join()

    print("Done")

