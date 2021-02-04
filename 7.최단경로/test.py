'''
다익스트라 알고리즘
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
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
            

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF: print('INF')
    else: print(distance[i])