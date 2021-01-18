# 1096 바둑판에 흰 돌 놓기 (19x19)
# n = int(input())
# board = [[0]*19 for _ in range(19)]

# for _ in range(n):
#     x, y = input().split()
#     x = int(x)
#     y = int(y)
#     board[x-1][y-1] = 1

# for i in range(19):
#     for j in range(19):
#         print(board[i][j], end=" ")
#     # print(end="\n")
#     print()


# 1097 바둑알 십자 뒤집기
# board = [[0]*19 for _ in range(19)]
# for i in range(19):
#     board[i] = input().split()
#     board[i] = list(map(int, board[i]))

# n = int(input())

# while n > 0:
#     x, y = input().split()
#     x = int(x)
#     y = int(y)

#     for i in range(19):
#         for j in range(19):
#             if i == x-1 or j == y-1:
#                 board[i][j] = int((not board[i][j]))

#     board[x-1][y-1] = int((not board[x-1][y-1]))


#     n-=1

# for i in range(19):
#     for j in range(19):
#         print(board[i][j], end=" ")
#     print()

# 1098 설탕과자 뽑기
# h, w = input().split()  # 세로, 가로
# n = int(input())

# board = [[0]*int(w) for _ in range(int(h))]

# for _ in range(n):
#     l, d, x, y = input().split()
#     l = int(l)
#     d = int(d)
#     x = int(x)
#     y = int(y)
#     x -= 1
#     y -= 1
#     Y = y
#     X = x

#     if d == 0:
#         for t in range(l):
#             print(X, Y)        
#             if X < int(w)-1/2:  
#                 board[x][y] = 1
#                 y+=1
#             else:
#                 board[x][y] = 1
#                 y-=1

#     else:
#         for t in range(l):
#             print(X, Y)        
#             if Y < int(h)-1/2:  
#                 board[x][y] = 1
#                 x+=1
#             else:
#                 board[x][y] = 1
#                 x-=1


# #출력하기
# for i in range(len(board)): #가로
#     for j in range(len(board[i])):  #세로
#         print(board[i][j], end=' ')
#     print()

############## 사이트 풀이 ############
# a,b=input().split()
# h=int(a)
# w=int(b)

# m=[]
# for i in range(h+1) :
#     m.append([])
#     for j in range(w+1) :
#         m[i].append(0)

# n=int(input())

# for i in range(n) :
#     l,d,x,y=input().split()
#     for j in range(int(l)) :
#         if int(d)==0 :
#             m[int(x)][int(y)+j]=1
#         else :
#             m[int(x)+j][int(y)]=1


# for i in range(1, h+1) :
#     for j in range(1, w+1) :
#         print(m[i][j], end=' ')
#     print()    
######################################

# 1099 성실한 개미
# 0(갈 수 있는 곳), 1(벽 또는 장애물), 2(먹이)
# 단, 맨 아래 가장 오른쪽: 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우 머무르게 되는 곳
board = []
for i in range(10):
    info = list(map(int, input().split()))
    board.append(info)



