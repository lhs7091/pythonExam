def promising(i):
    for j in range(0, i):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[j] == row[i] or abs(row[j] - row[i]) == (i - j):
            return False
    return True


def N_queen(i):
    global result
    if i == N:
        result += 1
    else:
        for j in range(N):
            row[i] = j
            if promising(i):
                N_queen(i + 1)


N = int(input())
row = [0] * 15
result = 0
N_queen(0)
print(result)

