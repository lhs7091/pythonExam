import sys

N = 0
result = []

def fibonacci(index):
    if index == N:
        return
    result.append(result[index-1]+result[index])
    fibonacci(index+1)


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    result.append(0)
    result.append(1)
    fibonacci(1)
    sys.stdout.write(str(result[-1]))
