'''
2. 미래도시 1번회사 -> K회사 들른 후 -> X회사 마지막으로 가는 최소 수
플로이드 워샬
4 2
1 3
2 4
3 4

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][K] + graph[K][X]

if distance >= INF: print("-1")
else: print(distance)
