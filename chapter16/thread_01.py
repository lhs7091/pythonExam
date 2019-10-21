import _thread
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay) # delay second
        count += 1
        print(nameOfThread, "~~~~~~~", time.time())

try:
    _thread.start_new_thread(print_epoch, ("thread 1", 2))
    _thread.start_new_thread(print_epoch, ("thread 2", 4))
except:
    print("this is an error")

# input() #thread를 내부에서 실행하기 위한 함수

while 1:
    pass # 무한루프