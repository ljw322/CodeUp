'''
요약: 도시N, 통로M, 메세지 보낼 도시 C, 단방향 가중치(X, Y, Z)
    출력 -> 도시 C에서 메세지를 받는 도시의 총 개수와 총 걸리는 시간?
해결: graph와 heapq의 차이점 인지하라.
3 2 1
1 2 4
1 3 2
'''
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())
distance = [INF]*(N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        
        for i in graph[now]:
            c = cost + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))

dijstra(C)

# distance에 대하여 처리

result = 0
maxValue = -1
for value in distance:
    if value != INF and value != 0:
        result += 1
    if value != INF and maxValue <= value:
        maxValue = value

print(result, maxValue)