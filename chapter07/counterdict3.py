from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

print("c+d=", c+d)
#c.subtract(d)
#print("c-d=", c)

print(c&d)
print(c|d)