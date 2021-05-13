# 21 05 13 15:12 ~ 16:00 (50분) 쉬워보이는데..? 50분 걸림. BFS

'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
from collections import deque
n, k = map(int, input().split())
board = []
# queue = deque()
virusPos = [[] for i in range(k+1)]

# 초기 맵정보 입력받기
for i in range(n):
    tempList = list(map(int, input().split()))
    board.append(tempList)

# 초기 바이러스 위치 파악하기
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virusPos[board[i][j]].append((i, j))

s, X, Y = map(int, input().split())

#################입력셋팅 완료#################

print(virusPos)

# 시계방향
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

List = []
for _ in virusPos:
    List.append(deque(_)) 

print(List)

# 주어진 초 만큼 실행
while s > 0:

    for virus in range(1, k+1):
        print("virus:",virus)
        
        count = len(List[virus])
        for virusNum in range(1, count+1):
            x, y = List[virus].popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[nx][ny] == 0:
                    board[nx][ny] = virus
                    List[virus].append((nx,ny))
                    print(virusNum, ":", x, y, "->", nx, ny)



    s -= 1


for i in range(n):
    for j in range(n):
        print(board[i][j], end="")
    print()

print(board[X-1][Y-1])