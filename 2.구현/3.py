'''
3. 게임 개발 40분 1초 128MB 14:45 ~ 15:25
캐릭터가 방문한 '칸'의 수
0: 갈 수 있는 길, 1: 바다 
네 방향 모두 갈 수 있는 곳 없으면 뒤로 돌아오기. 뒤가 바다면 종료
'''
n, m = map(int, input().split())
visit = [[0]*m for i in range(n)]  # 방문 정보 모두 0으로 초기화

x, y, direction = map(int, input().split())
# 현재 있는 위치 방문처리
visit[x][y] = 1

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 0인 곳 가기
    if visit[nx][ny] == 0 and board[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 갈 수 있는 곳 아니면 회전
    else:
        turn_time += 1

    # 네 방향 모두 다 돌았다면 뒤로
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 뒤로
        if board[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다이면 종료
        else:
            break
        turn_time = 0

print(count)

        


