# 설탕공장 설탕배달중
# 봉지 단위는 5kg, 3kg
# 최소한의 봉지를 들고가기 위한 방법
# input
#  18
# output
#  4

import sys

N = int(sys.stdin.readline())

# 지연 시간 확인 시작!
import time
start = time.time() # 시작 시간을 start라는 변수에 저장

# 최종 봉지수
result = 0
# 봉지단위
packages = [5,3]

if(N%5 != 0):
    while True:
        if(N<3): 
            result = -1
            break
        result += 1
        N -= 3
        if(N%5==0):
            result += N//5
            break
else:
    result += N//5

print('result : {}'.format(result))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 