# 21 05 21 14:50 ~ 15:40 못품.
# 상하좌우 방향따로, 회전 따로 계산해서 next_pos 리스트에 추가해서 반환.
from collections import deque

def getNextPos(pos, board):
    next_pos = []
    pos = list(pos) # 집합 형태를 리스트 형태로 변환
    
    ax, ay, bx, by = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nax, nay, nbx, nby = ax+dx[i], ay+dy[i], bx+dx[i], by+dy[i]
        
        if board[nax][nay] == 0 and board[nbx][nby] == 0:
            next_pos.append({(nax,nay),(nbx,nby)})
            
        # 로봇이 현재 가로일 때
        if ax == bx:
            for i in [-1,1]:
                #위 또는 아래 0인지 확인(회전할 수 있는지 확인)
                if board[ax+i][ay] == 0 and board[bx+i][by] == 0:
                    next_pos.append({(ax,nay),(ax+i,ay)})
                    next_pos.append({(bx,nby),(bx+i,by)})
        
        # 로봇이 현재 세로일 때
        elif ay == by:
            for i in [-1,1]:
                #좌 또는 우가 0인지 확인(회전할 수 있는지 확인)
                if board[ax][ay+i] == 0 and board[bx][by+i] == 0:
                    next_pos.append({(ax,ay),(ax,ay+i)})
                    next_pos.append({(bx,by),(bx,by+i)})
                    
    return next_pos
                
def solution(board):
    
    n = len(board)
    new_board = [[1]*(n+2) for i in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    visited.append(pos)
    q.append((pos, 0))
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in getNextPos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    
    return 0