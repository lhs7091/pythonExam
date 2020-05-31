import itertools
import sys

N = 0
scoreBoard = []

def calcScore(member):
    allMember = [i for i in range(N)]
    start_team = []
    link_team = []

    for i in allMember:
        if i in member:
            start_team.append(i)
        else:
            link_team.append(i)

    start_sum = 0
    for i in start_team:
        for j in start_team:
            start_sum += scoreBoard[i][j]

    link_sum = 0
    for i in link_team:
        for j in link_team:
            link_sum += scoreBoard[i][j]

    return abs(start_sum-link_sum)


def solve(players):
    # all of possibility
    combination_members = itertools.combinations(players, int(N/2))
    selected_members = list(combination_members)
    length = int(len(selected_members)/2)

    minVal = sys.maxsize
    for member in selected_members[:length]:
        result = calcScore(member)

        if minVal>result: minVal=result

    sys.stdout.write(str(minVal))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    players = [i for i in range(N)]
    for i in range(N):
        scoreBoard.append(list(map(int, sys.stdin.readline().split())))
    solve(players)