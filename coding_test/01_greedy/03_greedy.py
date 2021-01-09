# 각 자리숫자가 0부터 9까지로만 이루어진 문자열 S가 주어짐
# 왼쪽부터 오른쪽으로 순서대로 숫자 확인
# 숫자 사이사이에 곱하기 또는 더하기 연산자를 넣음
# 연산결과 가장 큰 값이 나오도록 프로그램 작성

import sys

N = sys.stdin.readline()

# 지연 시간 확인 시작!
import time
start = time.time() # 시작 시간을 start라는 변수에 저장

result = int(N[0])

for i in range(1, len(N)-1):
    num = int(N[i])
    if num<=1 or result <=1:
        result += num
    else:
        result *=num

print('result : {}'.format(result))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 