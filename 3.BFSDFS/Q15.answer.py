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
distance = [-1]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


q = deque([x])
distance[x] = 0

while q:
    node = q.popleft()

    for v in graph[node]:
        if distance[v] == -1:
            cost = distance[node] + 1
            distance[v] = cost
            q.append(v)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)