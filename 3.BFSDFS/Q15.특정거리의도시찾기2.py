# 2021 06 18 18:35 ~ 
'''
요약: N개의 도시와 단방향 M, 최소 거리가 K인 도시를 오름차순으로 출력. 없으면 -1. (거리는 모두 1)
해결: 다익스트라 이용한다.
    1. deque, INF, graph
    2. dijstra
        1). 시작점 deque에 넣기, distance 0으로 초기화
        2). q존재 할 때까지.
            거리계산.
            계산 거리가 다음의 거리보다 작으면 distance갱신과, q에 append

효율적인 다익스트라는 heapq를 쓴다.(도시간 거리 비중값이 다양하기 때문이다.)
이 문제는 모든 거리가 1 이므로 deque를 이용해서 푼 것이다.
'''
from collections import deque
INF = int(1e9)
n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijstra(start):
    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        node = q.pop()
        for v in graph[node]:
            cost = distance[node] + 1
            if cost < distance[v]:
                distance[v] = cost
            q.append(v)
dijstra(x)

answer = []
# print(distance)


index = 0
for value in distance:
    if value == k:
        answer.append(index)
    index += 1

if answer:
    for value in answer:
        print(value)

else: print(-1)