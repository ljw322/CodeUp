'''
3. 게임 개발 40분 1초 128MB 14:45 ~ 15:25

'''
n, m = map(int, input().split())
visit = [[0]*(m + 1)for i in range(n + 1)]  # 방문 정보 모두 0으로 초기화

board = []
x_current, y_current, dict_current = map(int, input().split())
for i in range(n):
    board.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


