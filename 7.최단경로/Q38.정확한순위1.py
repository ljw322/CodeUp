# 21 05 24 13:25 ~ 14:00 (40분 제한)
'''
중요.
n명의 서로다른 성적비교. 이들 중 정확히 순위를 매길 수 있는 개수는?
플로이드워샬을 이용한다. 방향그래프 a -> b인데, k를 거쳐 갈 수 있는지 확인하기 위해서!
갈 수 있다면 성적을 비교할 수 있다는 것.

6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(n):
        if i == j: graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0

for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF: count += 1
    if count == n:
        result+=1

print(result)