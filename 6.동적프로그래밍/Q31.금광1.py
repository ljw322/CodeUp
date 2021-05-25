# 21 05 24 23:18 ~ 23:48(30분)
'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
T = int(input())

while T > 0:

    n, m = map(int, input().split())

    goldMap = [[0]*(m) for i in range(n)]
    info = list(map(int, input().split()))
    for i in range(n*m):
        goldMap[i//m][i%m] = info[i]

    # '열'씩 오른쪽으로 이동이다. (초기 첫번째 열은 그대로 둔다.)
    # 왼쪽 위, 왼쪽, 왼쪽 아래에서 오는 것들을 확인. 
    for j in range(1, m):
        for i in range(n):

            # 왼쪽 위 저장. (단, x행이 젤 위에 있을 때는 0)
            if i == 0:
                left_up = 0
            else:
                left_up = goldMap[i-1][j-1]

            # 왼쪽 아래 저장. (단, x행이 젤 아래에 있을 때는 0)
            if i == n-1:
                left_down = 0
            else:
                left_down = goldMap[i+1][j-1]

            left = goldMap[i][j-1]

            goldMap[i][j] = goldMap[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, goldMap[i][m-1])

    print(result)



    T -= 1
