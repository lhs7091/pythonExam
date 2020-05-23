'''import sys
n = int(sys.stdin.readline())
text = list()
for i in range(n):
    a, b = sys.stdin.readline().split()
    text.append((int(a), int(i), b))

text = sorted(text)

for age, _, name in text: sys.stdout.write(str(age)+" "+name+"\n")'''

import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])
