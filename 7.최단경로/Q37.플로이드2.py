'''
요약: n개도시, m개버스 간선비용. 모든 도시의 쌍에 대해 a->b 최소비용?
해결: 플로이드워샬!
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j: graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()