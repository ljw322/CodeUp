# 21 05 14 15:40 ~ 16:40 1시간만에 풀었으나. 틀. 틀린부분 찾아냄

n = int(input())

board = []
teachPos = []
studentNum = 0

for i in range(n):
    board.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            studentNum += 1
        if board[i][j] == 'T':
            teachPos.append([i,j])


# print(studentNum)
# print(teachPos)
answer = 'NO'

def checkNum(board):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                count += 1
    return count

def beam(board):
    global teachPos

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    end = [-1, n, n, -1]

    for teacher in teachPos:
        x, y = teacher
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            # 방향대로 레이저 쏘기. 'O'를 만날 때까지
            if dx[i] == 0: # y방향으로 쏘기
                if dy[i] == 1: m = abs(n-1-y)
                else: m = y
            else:   #x방향으로 쏘기
                if dx[i] == 1: m = abs(n-1-x)
                else: m = x

            for r in range(m):
                
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    break
                if board[nx][ny] == 'O':
                    break
                elif board[nx][ny] == 'S':
                    board[nx][ny] = 'X'
                nx += dx[i]
                ny += dy[i]



    return board

def dfs(count):
    temp = [['A']*(n+1) for _ in range(n+1)]
    global studentNum, answer

    if count == 3:
        # temp에 board옮기기
        for i in range(n):
            for j in range(n):
                temp[i][j] = board[i][j]

        # T위치별로 레이저 쏘기
        temp2 = beam(temp)

        # S의 갯수 확인
        if checkNum(temp2) == studentNum:
            answer = 'YES'

    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    board[i][j] = 'O'
                    count+=1
                    dfs(count)
                    count-=1
                    board[i][j] = 'X'

dfs(0)

print(answer)
