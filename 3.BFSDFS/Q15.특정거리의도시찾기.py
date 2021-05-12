# 2021 05 12 12:53 ~ 13:23.... 28 (5분초과.)
'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

# 최단거리 저장할 리스트
INF = 1e9
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

def bfs(start):
    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        node = q.popleft()

        for v in graph[node]:
            cost = distance[node] + 1
            if cost < distance[v]:
                distance[v] = cost
            q.append(v)

bfs(x)
print(distance)

answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for _ in answer:
        print(_)