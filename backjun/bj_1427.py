import sys

N = sys.stdin.readline()

for i in reversed(sorted(N)):
    sys.stdout.write(i)