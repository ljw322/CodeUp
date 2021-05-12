# 21 05 12 14:13 ~ 53 (틀! DFS로 풀어야 함.) ~ 15:11
'''
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''

n, m = map(int, input().split())

board = []
temp = [[-1]*(m) for i in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x,y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx,ny)


def countSpce():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: count += 1

    return count

def dfs(count):
    global result

    # 벽 세개를 다 세웠을 떄
    if count == 3:
        # temp로 옮겨서 확인하기
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        # 바이러스 확산시키기
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    virus(i,j)

        # 빈 칸 갯수 세기 
        # 갯수 비교해서 result
        result = max(result, countSpce())
    
        #확인할거 다 했으니 리턴
        return

    # 벽 세개 다 채우기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1

                dfs(count)
                board[i][j] = 0
                count -= 1



dfs(0)
print(result)