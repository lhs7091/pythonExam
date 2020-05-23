import sys
N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
outPut = []
result = list()

def solve(depth, N, M):
    if depth == M:
        result.append(' '.join(map(str, sorted(outPut))))
        #sys.stdout.write(' '.join(map(str, outPut)))
        #sys.stdout.write("\n")
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            outPut.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            outPut.pop()


solve(0, N, M)

for j in sorted(set(result)):
    sys.stdout.writelines(j+"\n")

