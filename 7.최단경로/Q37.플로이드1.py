# 21 05 24 플로이드 12:01 ~ 13:21 (40분 제한)
# https://www.acmicpc.net/problem/11404
'''
도시개수
버스개수
a -> b로 가는 최소 비용계산

5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(n):
    for j in range(n):
        if i == j: graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)



for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()