import sys

N = int(sys.stdin.readline())

row = [0] * 15
result = 0

def queen(level):
    global result
    if level == N: result += 1
    else:
        for i in range(N):
            row[level] = i
            if promising(level):
                queen(level+1)


def promising(level):
    for i in range(0, level):
        if row[i] == row[level] or abs(row[i]-row[level]) == (level-i):
            return False
    return True


queen(0)
sys.stdout.writelines(str(result))
