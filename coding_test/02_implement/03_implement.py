# 알파벳 대문자와 숫자로믄 구성된 문자열 입력
# 알파벳은 오름차순 정렬
# 숫자는 모두 더해서 결과를 알파벳 다음 출력
# input 최대10000개
#  K1KA5CB7 // AJKDLSI412K4JSJ9D
# output
#  ABCKK13 // ADDIJJJKKLSS20

import time

data = input()
stringList = []
sum = 0

for x in data:
    if x.isalpha():
        stringList.append(x)
    else:
        sum+=int(x)

stringList.sort()

if (sum != 0):
    stringList.append(str(sum))

# 리스트를 문자열로 변환하여 출력
print(''.join(stringList))
