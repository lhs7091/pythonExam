import sys

input = sys.stdin.readline

def checkRow(nx, i):
    if i in row[nx]: return False
    return True


def checkCol(ny, i):
    for index in range(9):
        if i == row[index][ny]:
            return False
    return True


def check3X3(x, y, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == row[nx+i][ny+j]:
                return False
    return True


def sudoku(index):
    if index == len(zeros):
        for line in row:
            for n in line:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]

            if checkRow(nx, i) and checkCol(ny, i) and check3X3(nx, ny, i):
                row[nx][ny] = i
                sudoku(index+1)
                row[nx][ny] = 0


row = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if row[i][j] == 0]
sudoku(0)
