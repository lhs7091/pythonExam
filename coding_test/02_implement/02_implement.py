# N x N 정사각형 2차원 공간
# 가장 왼쪽 위 (1,1)
# 가장 오른쪽 아래 (N,N)
# 이동 후 최종 좌표 구하기
# input
#  5
#  R R R U D D
# output
#  3 4

import time

# 2차원 공간 크기
N = int(input())

# 좌표 시작점
x, y = 1,1
# 움직이는 순서
orders = input().split()

# 시간측정
startTime = time.time()

# L R U D 이동 순서
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type=['L', 'R', 'U', 'D']

for order in orders:
    for i in range(len(move_type)):
        if order == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny<1 or nx>N or ny>N:
        continue
    x, y = nx, ny

print('result : ({},{})'.format(str(x), str(y)))

print("time : ", time.time() - startTime) 

