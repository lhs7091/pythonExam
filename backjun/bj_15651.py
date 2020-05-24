import sys
N, M = map(int, sys.stdin.readline().split())

temp = []
result = list()

def solve(depth):
    if depth == M:
        result.append(' '.join(map(str, temp)))
        return

    for i in range(N):
        temp.append(i+1)
        solve(depth+1)
        temp.pop()


solve(0)
for s in result:
    sys.stdout.writelines(s+"\n")
