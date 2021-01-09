# 어떤수 N이 1이 될때까지 하기 두가지 과정을 반복
# 최소 횟수는 몇회인가?
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다

import sys

N, K = map(int, sys.stdin.readline().split())

# 지연 시간 확인 시작!
import time
start = time.time() # 시작 시간을 start라는 변수에 저장

result = 0

while True:
    N -= 1
    N //= K
    result +=1
    if(N==0):
        break

print('result : {}'.format(result))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 