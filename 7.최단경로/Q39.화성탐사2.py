'''
요약: testcase T, N, N*N배열. [0][0]->[n-1][n-1] 까지 최단거리?
해결: 다익스트라 2차원 버전!!
    distance도 2차원!
    graph에 2차원 맵 정보를 저장한다.
    for i in graph[now] 가 아니라, dx dy 4방향 체크!
    
'''

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

T = int(input())

def dijstra(sx, sy, distance, graph, N):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = []
    heapq.heappush(q, (graph[sx][sy], sx, sy))
    distance[sx][sy] = graph[sx][sy]

    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
            continue

        # 네 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            c = cost + graph[nx][ny]
            if c < distance[nx][ny]:
                distance[nx][ny] = c
                heapq.heappush(q, (c, nx, ny))



while T > 0:

    N = int(input())
    distance = [[INF]*(N) for i in range(N)]
    graph = []
    
    for i in range(N):
        graph.append(list(map(int, input().split())))


    dijstra(0, 0, distance, graph, N)
    
    #출력
    print(distance[N-1][N-1])

    
    T-=1

