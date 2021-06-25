'''
요약: N개의 헛간, M개의 양방향 통로. 최단 거리가 가장 먼 헛간은?
    출력-> 숨어야하는 헛간번호(여러개면 가장 작은 거 출력),
            그 헛간까지의 거리 출력,
            그 헛간과 같은 거리를 갖는 헛간개수 출력
해결: 다익스트라로 일단 출력해서 가장 긴 거 출력?
    
'''

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
distance = [INF]*(N+1)
graph = [[]for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if cost < distance[now]:
            continue

        for i in graph[now]:
            c = cost + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))



dijstra(1)


result = distance[1:]
print(result)
maxValue = max(result)
print(result.index(maxValue)+1, maxValue, result.count(maxValue))
