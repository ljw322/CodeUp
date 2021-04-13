# from collections import deque

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
        
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# bfs(graph, 1, visited)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
    
#     #현재 노드에 현결된 노드들 재귀로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)

# 3 아이스크림 얼려먹기. dfs 상하좌우로 탐색할 것임
'''
4 5
00110
00011
11111
00000
'''
# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(
#         list(map(int, input()))
#         )

# def dfs(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False

#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True

#     return False

# count = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             count += 1

# print(count)


# 4. 미로 탈출 bfs
'''
3 3
110
010
011

5 6
101010
111111
000001
111111
111111
'''
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 탐색방향 설정. 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
            else:
                continue

bfs(0, 0)
print(graph[n-1][m-1])





