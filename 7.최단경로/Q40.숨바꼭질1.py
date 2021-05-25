# 21 05 24 19:20 ~ 17:50 (40분)
'''
다익스트라, 최단거리가 아닌, 최장거리
플로이드
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))


def dijstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start)) #(cost, node)

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for i in graph[node]:
            c = cost + i[0]
            if c < distance[i[1]]:
                distance[i[1]] = c
                heapq.heappush(q, (c, i[1]))


dijstra(1)
tempMax = []
for value in distance:
    if value != INF:
        tempMax.append(value)
maxValue = max(tempMax)
count = 0
minIndex = INF

for i in range(1, n+1):
    if maxValue == distance[i]:
        minIndex = min(i, minIndex)
        count += 1

print(distance)
print(minIndex, maxValue, count)

