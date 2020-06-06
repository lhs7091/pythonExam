import sys

N = 0
result = [1,1,1]
MAX = 100

def fibonacci(num, index):
    if index == MAX:
        return
    elif index == num:
        return
    result.append(result[index-2]+result[index-1])
    fibonacci(num, index+1)


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for i in range(N):
        num = int(sys.stdin.readline())
        if len(result) < num:
            fibonacci(num, len(result)-1)
        sys.stdout.write(str(result[num-1])+"\n")
