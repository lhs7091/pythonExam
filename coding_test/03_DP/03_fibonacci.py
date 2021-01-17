# memoization 방식
# 변수 2개반 사용하여 메모리 절약
# if N = 40일 경우
# 결과 = 102334155
# 걸리는 시간 = 3.0040740966796875e-05초

import time

start = time.time()

memo = {1:1, 2:1}
def fib(n):
    a, b = 1,0
    for i in range(n):
        a,b = b, a+b
    return b

N = 40
print(fib(N))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 