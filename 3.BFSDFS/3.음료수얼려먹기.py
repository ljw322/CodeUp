'''
3. 음료수 얼려먹기 30분 1초 128MB 14:40~15:10
n*m 에서 생성되는 아이스크림의 개수는? -> DFS !
board를 돌면서 dfs를 진행한다.
'''
n, m = map(int, input().split())

# 그래프 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS
def dfs(x, y):
    # 종료조건
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 이어져 있는 부분이 있다면 상하좌우 탐색 후 True
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리!
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)       
        return True
    return False

# 함수 호출
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)