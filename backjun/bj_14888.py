import sys

N = int(sys.stdin.readline())
num = [int(i) for i in sys.stdin.readline().split()]
oper = [int(i) for i in sys.stdin.readline().split()]
res_max = -1000000000
res_min = 1000000000


def dfs(val, depth):
    global res_min, res_max

    if depth == N-1:
        if res_min > val: res_min = val
        if res_max < val: res_max = val
        return

    for i in range(len(oper)):
        if oper[i] != 0:
            oper[i] -= 1
            if i == 0:
                dfs(val+num[depth+1], depth+1)
            elif i == 1:
                dfs(val - num[depth + 1], depth + 1)
            elif i == 2:
                dfs(val * num[depth + 1], depth + 1)
            elif i == 3:
                dfs(int(val / num[depth + 1]), depth + 1)
            oper[i] += 1


dfs(num[0], 0)
sys.stdout.write(str(res_max)+"\n"+str(res_min));
