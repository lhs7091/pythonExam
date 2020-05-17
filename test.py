
N = int(input())
'''
1 2
3 4 
5 6
7 8 9 
10 11 12


x y distance    count
1 2 1           1   1   n+1/2 
1 3 2           11  2   n+1/2 +1

1 4 3           111 3   n+1/2 +1
1 5 4           121 3   n+1/2 +1
1 6 5           1211 4  
1 7 6           1221 4

1 8 7           12211 5 
1 9 8           12221 5
1 10 9          12321 5
1 11 10         123211 6
1 12 11         123221 6
     12                6
     
1 n+1/2
2 n+1/2
33 n+1/2
44 n+1/2

555 n+1/2
666

7777
8888
9999
10101010 


'''


'''def getDistance(x, y):
    count = 0
    if x == 0:
        while x != y:
            x += 1
            count += 1
        return count
    else:
        x += 2
        count += 1
        while x != y:
            x += 1
            count += 1
        return count'''
def getDistance(x, y):
    if y-x == 1: return 1
    else: return (y-x)/2+1


count = []
for i in range(N):
    x, y = input().split()
    count.append(getDistance(int(x), int(y)))


for j in count: print(int(j))










# N number of card
# M maximum sum

'''N, M = input().split()
card = input().split(" ")
M = int(M)
length = len(card)

def get_total():
    maximum = 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                sum = int(card[i])+int(card[j])+int(card[k])
                if maximum <= sum <= M:
                    maximum = sum
    print(maximum)


get_total()'''


'''
10
65
100
30
95
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)'''


'''
print((a+b)%c)
print((a%c)+(b%c)%c)
print((a×b)%c)
print(((a%c) × (b%c))%c)
print(int(a)%int(b))
'''