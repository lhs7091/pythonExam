# memoization 방식
# if N = 40일 경우
# 결과 = 102334155
# 걸리는 시간 = 4.792213439941406e-05초

import time

start = time.time()

memo = {1:1, 2:1}
def fib(n):
    if n in memo: 
        return memo[n]
    else: 
        f = fib(n-1)+fib(n-2)
        memo[n] = f
    return f

N = 10
print(fib(N))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 
    