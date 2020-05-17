import sys
n = int(sys.stdin.readline())
text = list()

for i in range(n):
    text.append(sys.stdin.readline())

text = list(set(text))
sort_text = list()

for j in text: sort_text.append((len(j), j))

sort_text.sort()

for len_voca, voca in sort_text: sys.stdout.write(voca)
