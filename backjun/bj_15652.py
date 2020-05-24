import sys
N, M = map(int, sys.stdin.readline().split())

temp = []

def progression(depth, index, N, M):

    if depth == M:
        sys.stdout.write(' '.join(map(str, temp))+"\n")
        return

    for i in range(index, N):
        temp.append(i+1)
        progression(depth+1, i, N, M)
        temp.pop()


progression(0, 0, N, M)
