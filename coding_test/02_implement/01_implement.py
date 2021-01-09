# 정수 N을 입력
# 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
# 세어야 하는 시각
#  00시 00분 03초
#  00시 13분 30초
# 세면 안되는 시각
#  00시 02분 55초
#  01시 27분 45초

import sys
import time

# N시 input
N = int(sys.stdin.readline())

# 시작시간
startTime = time.time()

# 경우의 수
result = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                result +=1

print('result : {}'.format(result))

print("time : ", time.time() - startTime) 