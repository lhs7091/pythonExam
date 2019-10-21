from collections import Counter

text = list("gallahad")
print(text)

c = Counter(text)
print(c)

print(c["a"])