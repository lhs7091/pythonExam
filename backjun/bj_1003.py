import sys

N = 0
result = [0,1]


def fibonacci(index):
    if index == 40:
        return
    result.append(result[index-1]+result[index])
    fibonacci(index+1)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    fibonacci(1)
    for i in range(N):
        num = int(sys.stdin.readline())
        if num == 0:
            sys.stdout.write("1 0"+"\n")
            continue
        sys.stdout.write(str(result[num-1])+" "+str(result[num])+"\n")

