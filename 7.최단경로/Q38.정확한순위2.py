'''
요약: 학생들 성적 1:1비교로만 안다. 순위를 정확히 알 수 있는 학생은 몇명?
해결: 플로이드 워샬 응용!
    -> graph[i][j] != INF or graph[j][i] != INF 확인하면 된다.
'''
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = min(graph[a][b], 1)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result+=1
    
print(result)
