'''
4. 미로탈출 30분 1초 128MB 16:00~16:30
탈출하기까지의 최소 칸의 개수(시작,마지막점 포함) -> bfs
1이 갈 수 있는 곳
'''
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs(x, y):
    queue = deque()         # 큐 선언
    queue.append((x, y))      # 초기값 집어넣기
    while queue:            # queue에 값이 존재할때까지 bfs 시작!
        x, y = queue.popleft()

        # 네 방향으로 bfs 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어날 때 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 이동 시 최단 거리 graph에 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 최종 n,m위치 출력
    return graph[n-1][m-1]

# bfs 수행
print(bfs(0, 0))


