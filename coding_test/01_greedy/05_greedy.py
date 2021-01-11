# 백준 11399
# https://www.acmicpc.net/problem/11399


# 사람수
N = int(input())
# 각 사람의 돈 인출 시간
withdraw = list(map(int, input().split()))

# 시간 합계
result = 0

# 인출시간 순서대로 정렬
withdraw.sort()

#합계
for i in range(N):
    for j in range(i+1):
        result += withdraw[j]

print(result)
