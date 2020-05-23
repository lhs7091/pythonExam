import sys
N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
outPut = []

def solve(depth, N, M):
    if depth == M:
        sys.stdout.write(' '.join(map(str, outPut)))
        sys.stdout.write("\n")
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            outPut.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            outPut.pop()


solve(0, N, M)

'''
call 0 : add 1 //1
call 1 : skip 1, add 2 //1,2
call 2 : skip 1, skip 2, add 3 // 1,2,3
call 3 : skip 1, skip 2, skip 3, add 4 // 1,2,3,4
call 4 : depth4 = M4 print 1234
call 3 : remove 4 // 1,2,3
call 2 : remove 3, add 4 // 1,2,4
call 3 : skip 1, skip 2 skip

'''
