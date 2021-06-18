# 21 06 10,18 틀림
'''
요약: 뱀. 방향전환 왼,오. 자기자신에 닿거나 벽닿을 때 종료. 살아남은 시간은?
해결: 1. 방향전환 함수 turn(direction, c)
    2. 뱀위치저장은 리스트로. 맨앞이 꼬리부분. 쉽게 pop할 수 있게
    3. if 범위 안 and 자기자신 안닿을 때
            if 사과 아닐때
            else 사과 일때
       else 
    4. if 방향전환 조건 확인 변수 index

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
N = int(input())
board = [[0]*(N+1) for i in range(N+1)]

appleNum = int(input())
for i in range(appleNum):
    x, y = map(int, input().split())
    board[x][y] = 1

rotateNum = int(input())
rotateInfo = []
for i in range(rotateNum):
    t, c = input().split()
    rotateInfo.append((int(t), c))

x = 1
y = 1
board[x][y] = 's'

# 동쪽 방향 시작. 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
time = 0        #전체시간
index = 0       #방향회전 카운트
snake = [(x,y)] #꼬리가 맨 앞부분이다

def turn(direction, c):
    if c == 'L':
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4
    return direction


while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 범위안에 있고 머리가 아닐 때
    if 1 <= nx and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 's':
        # 빈 공간이면
        if board[nx][ny] == 0:
            board[nx][ny] = 's'
            snake.append((nx, ny))
            bx, by = snake.pop(0) # 꼬리 원상복귀!
            board[bx][by] = 0
        if board[nx][ny] == 1:
            board[nx][ny] = 's'
            snake.append((nx, ny))
    else:
        time += 1
        break

    x, y = nx, ny
    time += 1
    if index < rotateNum and time == rotateInfo[index][0]:
        direction = turn(direction, rotateInfo[index][1])
        index += 1


print(time)