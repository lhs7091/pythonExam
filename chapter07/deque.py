from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)

print(deque_list)

for i in range(len(deque_list)):
    deque_list.appendleft(i)

print(deque_list)

deque_list.rotate(2)
print(deque_list)