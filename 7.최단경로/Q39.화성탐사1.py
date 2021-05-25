# 21 05 24 14:05 ~ 14:45 (40분) 초과, 땡!
'''
특정지점 a 에서 b까지 가는 최소 비용 => 다익스트라.?
=> 다익스트라 기본형의 2차원 버전! distance배열을 2차원으로 잡고 양방향으로 bfs한다.

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
# 우선순위 큐
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

T = int(input())

def dijstra(sx, sy, distance, graph, N):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = []
    distance[sx][sy] = graph[sx][sy]
    heapq.heappush(q, (graph[sx][sy], 0, 0)) #(cost, node)

    while q:
        cost, x, y = heapq.heappop(q)

        if distance[x][y] < cost:
                continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            c = cost + graph[nx][ny]
            if c < distance[nx][ny]:
                distance[nx][ny] = c
                heapq.heappush(q, (c, nx, ny))


# 테스트 케이스 만큼 반복
while T > 0:

    N = int(input())
    distance = [[INF]*(N) for i in range(N)]
    graph = [[] for i in range(N)]

    # 그래프 정보 입력
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    dijstra(0, 0, distance, graph, N) # 0지점에서 출발
    
    print(distance[N-1][N-1])

    T -= 1