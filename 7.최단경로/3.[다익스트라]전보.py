'''
3.전보 다익스트라 1차원 distance정보에 INF가 아닌 것들의 갯수 및 시간 총합
시작점으로부터 각 지점까지 가는 최단경로 !
0. graph, distance 배열. graph에는 (cost, node)형태로 넣기
0. heapq에 큐, 시작점(0, node) 넣기, distance도
1. 큐에 꺼낸 후, 큐에 있는 것이 짧으면 pass
2. 다른 인접 노드들 확인
3. 새로운 cost 계산
4. 새로운 cost 더 짧으면, dist배열 갱신, heapq에 추가

3 2 1
1 2 4
1 3 2
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
start = c
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: 
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF: print('INF', end=" ")
#     else: print(distance[i], end=" ")

count = 0
maxValue = 0
for i in range(1, n+1):
    if i == start:
        continue

    if distance[i] != INF:
        count += 1

    if maxValue < distance[i]:
        maxValue = distance[i]

print(count, maxValue)
print(distance)