'''
3.전보 다익스트라 1차원 distance정보에 INF가 아닌 것들의 갯수 및 시간 총합

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