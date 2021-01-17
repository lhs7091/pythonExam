# 단순 알고리즘
# 재귀반복
# if N = 40일 경우
# 결과 = 102334155
# 걸리는 시간 = 12.505074262619019초
import time

start = time.time()
def fib(n):
    if n<=2 : return 1
    else : return fib(n-1)+fib(n-2)

N = 40
print(fib(N))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 