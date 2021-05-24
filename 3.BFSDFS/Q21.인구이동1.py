# 21 05 17 15:23~:37 (40분) 틀.
'''
3 5 10
10 15 20
20 30 25
40 22 10
'''
from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def moving(x, y, index):
    united = []
    united.append((x,y))
    q = deque()
    q.append((x,y))

    union[x][y] = index
    people = graph[x][y]
    count = 1

    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                # print(qx, qy, "->", nx, ny, ":", union[nx][ny])
                if l <= abs(graph[qx][qy]-graph[nx][ny]) <=r:
                    union[nx][ny] = index
                    q.append((nx,ny))
                    united.append((nx,ny))
                    count += 1
                    people += graph[nx][ny]


    for a, b in united:
        graph[a][b] = people//count

    return 


result = 0
while True:
    union = [[-1]*(n) for i in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                moving(i, j, index)
                index +=1

    
    if index == n*n:
        break
    result += 1

print(result)