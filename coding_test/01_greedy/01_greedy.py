# 거스름돈 문제
#  500원, 100원, 50원, 10원짜리 동전으로 거스름돈 걸러주기..
#  동전의 최소 개수는???
# n = xxxx원

# xxx 원
n = int(input())

# 지연 시간 확인 시작!
import time
start = time.time() # 시작 시간을 start라는 변수에 저장

# 동전의 갯수
answer = 0

# 화폐단위
money = [500,100,50,10]

for coin in money:
    answer += n // coin
    n %= coin

print('answer: {}'.format(answer))

# 종료 시점의 현재 시간(time.time()) 에서 시작 시간을 빼서 화면에 출력
print("time : ", time.time() - start) 

