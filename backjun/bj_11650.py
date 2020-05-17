import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))

for i in so:
    sys.stdout.writelines(str(i[0])+" "+str(i[1])+"\n")
