import threading
import time

def print_eopch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "~~~~~~~~~~", time.time())

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("start thread", self.name)
        print_eopch(self.name, self.delay)
        print("end thread", self.name)

if __name__ == "__main__":
    t1 = MyThread("Thread 1", 1)
    t2 = MyThread("Thread 2", 2)

    t1.start()
    t2.start()

    print(threading.active_count())
    print(threading.currentThread())
    print(threading.enumerate()) # 활성화된 thread list

    t1.join()
    t2.join()

    print("Done")