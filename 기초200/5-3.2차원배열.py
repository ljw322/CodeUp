# 1460 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-1
# n = int(input())

# s = 1
# for i in range(n):
#     for j in range(n):
#         print(s, end=" ")
#         s+=1
#     print()

# for i in range(0, n+1):
#     for j in range(n*i, n*i+4):
#         print(j+1, end=" ")
#     print()

# 1461 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-2
# n = int(input())
# for i in range(1, n+1):
#     for j in range(i*n, n*i-n, -1):
#         print(j, end=" ")
#     print()

# 이 코드가 더 깔끔한 것 같다.
# for i in range(1, n+1):
#     for j in range(0, n):
#         print(i*n-j, end=" ")
#     print()


# 1462 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-3
# n = int(input())
# for i in range(1, n+1):
#     for j in range(0, n):
#         print(j*n+i, end=" ")
#     print()

# 1463 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-4
# n = int(input())
# for i in range(0, n):
#     for j in range(1, n+1):
#         print(n*j-i, end=" ")
#     print()

# 1464 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-5
# n, m = map(int, input().split())
# s = n*m
# for i in range(n):
#     for j in range(m):
#         print(s, end=" ")
#         s-=1
#     print()

# 1465 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-6
# n:3, m:4 시작: 4n+1
# n, m = map(int, input().split())
# for i in range(n-1, -1, -1):
#     for j in range(1, m+1):
#         print(m*i+j, end=" ")
#     print()

# 1466 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-7
# n, m = map(int, input().split())
# for i in range(n*m, n*m-n, -1):
#     for j in range(m):
#         print(i+j*(-n), end=" ")
#     print()

# 1467 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-8
# n, m = map(int, input().split())
# for i in range(n*m-n+1, n*m+1):
#     for j in range(m):
#         print(i+j*(-n), end=" ")
#     print()

# 1468 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-1
# n = int(input())
# for i in range(1, n+1):
#     if i % 2 == 0:
#         for j in range(i*n, i*n-n, -1): print(j, end=" ")
#     else: 
#         for j in range(i*n-n+1, i*n+1): print(j, end=" ")
#     print()

# 1469 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-2
# n = int(input())
# for i in range(1, n+1):
#     if i % 2:
#         for j in range(i*n, i*n-n, -1): print(j, end=" ")
#     else: 
#         for j in range(i*n-n+1, i*n+1): print(j, end=" ")
#     print()

# 1470 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-3
# n = int(input())
# # 열 행 순서
# board = [[0]*n for i in range(n)]
# count = 1
# for i in range(0, n):
#     if i % 2 == 0:
#         for j in range(0, n):
#             board[j][i] = count
#             count+=1
#     else:
#         for j in range(n-1, -1, -1):
#             board[j][i] = count
#             count+=1

# for i in range(0, n):
#     for j in range(0, n):
#         print(board[i][j], end=" ")
#     print()

# 1471 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-4
# n = int(input())
# # 열 행 순서
# board = [[0]*n for i in range(n)]
# count = 1
# for i in range(0, n):
#     if i % 2:
#         for j in range(0, n):
#             board[j][i] = count
#             count+=1
#     else:
#         for j in range(n-1, -1, -1):
#             board[j][i] = count
#             count+=1

# for i in range(0, n):
#     for j in range(0, n):
#         print(board[i][j], end=" ")
#     print()

#################2차원배열 선언 연습################
# 1. n*n일때
# n = int(input())
# board = [[0]*n for i in range(n)]
# 2. n*m일때 [행 열] 열 행 순서
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()
###################################################

# 1472 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-3
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# count = 1
# for i in range(n-1, -1, -1):
#     if count%2 == 0:
#         for j in range(m):
#             board[i][j] = s
#             s+=1
#     else:
#         for j in range(m-1, -1, -1):
#             board[i][j] = s
#             s+=1
#     count+=1  
# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1473 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-6
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# count = 1
# for i in range(n-1, -1, -1):
#     if count%2 == 0:
#         for j in range(m-1, -1, -1):
#             board[i][j] = s
#             s+=1
#     else:
#         for j in range(m):
#             board[i][j] = s
#             s+=1
#     count+=1       
# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1474 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-7
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# count = 1
# for i in range(m-1, -1, -1):
#     if count%2:
#         for j in range(n-1, -1, -1):
#             board[j][i] = s
#             s+=1
#     else:
#         for j in range(n):
#             board[j][i] = s
#             s+=1
#     count+=1   
        

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1475 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-8
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# count = 1
# for i in range(m-1, -1, -1):
#     if count%2:
#         for j in range(n):
#             board[j][i] = s
#             s+=1
#     else:
#         for j in range(n-1, -1, -1):
#             board[j][i] = s
#             s+=1
#     count+=1   
        

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1476 : [기초-배열연습] 2차원 배열 빗금 채우기 3-1
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(0, n+m-1):
#     for i in range(0, m):
#         for j in range(0, n):
#             if i+j == k:
#                 board[j][i] = s
#                 s+=1       
# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1477 : [기초-배열연습] 2차원 배열 빗금 채우기 3-2
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(0, n+m-1):
#     for i in range(0, n):
#         for j in range(0, m):
#             if i+j == k:
#                 board[i][j] = s
#                 s+=1       

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1478 : [기초-배열연습] 2차원 배열 빗금 채우기 3-3
# 빗금채우기 3-2에서 출력반 뒤집어서 해주면 될 듯하다.
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(0, n+m-1):
#     for i in range(0, n):
#         for j in range(0, m):
#             if i+j == k:
#                 board[i][j] = s
#                 s+=1  
# for i in range(n):
#     for j in range(m-1, -1, -1):
#         print(board[i][j], end=" ")
#     print()

# 1479 : [기초-배열연습] 2차원 배열 빗금 채우기 3-4
# 빗금채우기 3-1에서 출력반 뒤집어서 해주면 될 듯하다.
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(0, n+m-1):
#     for i in range(0, m):
#         for j in range(0, n):
#             if i+j == k:
#                 board[j][i] = s
#                 s+=1  

# for i in range(n):
#     for j in range(m-1, -1, -1):
#         print(board[i][j], end=" ")
#     print()

# 1480 : [기초-배열연습] 2차원 배열 빗금 채우기 3-5
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(n+m-2, -1, -1):
#     for i in range(m-1, -1, -1):
#         for j in range(n-1, -1, -1):
#             if i+j == k:
#                 board[j][i] = s
#                 s+=1       

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1481 : [기초-배열연습] 2차원 배열 빗금 채우기 3-6
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(n+m-2, -1, -1):
#     for i in range(n-1, -1, -1):
#         for j in range(m-1, -1, -1):
#             if i+j == k:
#                 board[i][j] = s
#                 s+=1       

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1481 : [기초-배열연습] 2차원 배열 빗금 채우기 3-7
# 빗금채우기 3-6에서 출력반 뒤집어서 해주면 될 듯하다.
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(n+m-2, -1, -1):
#     for i in range(n-1, -1, -1):
#         for j in range(m-1, -1, -1):
#             if i+j == k:
#                 board[i][j] = s
#                 s+=1       

# for i in range(n):
#     for j in range(m-1, -1, -1):
#         print(board[i][j], end=" ")
#     print()

# 1482 : [기초-배열연습] 2차원 배열 빗금 채우기 3-8
# 빗금채우기 3-5에서 출력반 뒤집어서 해주면 될 듯하다.
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
# s = 1
# for k in range(n+m-2, -1, -1):
#     for i in range(m-1, -1, -1):
#         for j in range(n-1, -1, -1):
#             if i+j == k:
#                 board[j][i] = s
#                 s+=1       

# for i in range(n):
#     for j in range(m-1, -1, -1):
#         print(board[i][j], end=" ")
#     print()

# 1484 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-1
# https://mungto.tistory.com/63 참고함
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = 0
# y = -1
# reverse = 1 # 처음엔 y증가시켜야

# limit = 0
# s = 1
# while s <= n*m:
#     for i in range(m - limit):      # 가로 채우기
#         # print(x, y)
#         y += reverse
#         board[x][y] = s
#         s+=1
        
#     for i in range(n - limit -1):   # 세로 채우기
#         # print(x, y)
#         x += reverse
#         board[x][y] = s
#         s+=1        
    
#     limit += 1
#     reverse *= -1


# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1485 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-2
# n*m 부터 시작해서 감소하는 방향으로
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = 0
# y = -1
# reverse = 1 # 처음엔 y증가시켜야

# limit = 0
# s = n*m
# while s >= 1:
#     for i in range(m - limit):      # 가로 채우기
#         # print(x, y)
#         y += reverse
#         board[x][y] = s
#         s-=1
        
#     for i in range(n - limit -1):   # 세로 채우기
#         # print(x, y)
#         x += reverse
#         board[x][y] = s
#         s-=1        
    
#     limit += 1
#     reverse *= -1


# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1486 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-3
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = -1
# y = m-1
# reverse = 1 # 처음엔 x증가시켜야

# limit = 0
# s = 1
# while s <= n*m:
#     for i in range(n - limit):   # 세로 채우기
#         x += reverse
#         board[x][y] = s
#         s+=1     

#     reverse *= -1

#     for i in range(m - limit -1):      # 가로 채우기
#         y += reverse
#         board[x][y] = s
#         s+=1    
          
#     limit += 1
    


# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1487 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-4
# n*m 부터 시작해서 감소하는 방향으로
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = -1
# y = m-1
# reverse = 1 # 처음엔 x증가시켜야

# limit = 0
# s = n*m
# while s >= 1:
#     for i in range(n - limit):   # 세로 채우기
#         x += reverse
#         board[x][y] = s
#         s-=1     

#     reverse *= -1

#     for i in range(m - limit -1):      # 가로 채우기
#         y += reverse
#         board[x][y] = s
#         s-=1    
          
#     limit += 1
    


# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1488 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-5
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = n-1
# y = m
# reverse = -1 # 처음엔 y 감소시켜야

# limit = 0
# s = 1
# while s <= n*m:
#     for i in range(m - limit):      # 가로 채우기
#         y += reverse
#         board[x][y] = s
#         s+=1    

#     for i in range(n - limit -1):   # 세로 채우기
#         x += reverse
#         board[x][y] = s
#         s+=1     
      
#     reverse *= -1
#     limit += 1

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1489 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-6
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = n-1
# y = m
# reverse = -1 # 처음엔 y 감소시켜야

# limit = 0
# s = n*m
# while s >= 1:
#     for i in range(m - limit):      # 가로 채우기
#         y += reverse
#         board[x][y] = s
#         s-=1    

#     for i in range(n - limit -1):   # 세로 채우기
#         x += reverse
#         board[x][y] = s
#         s-=1     
      
#     reverse *= -1
#     limit += 1

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1490 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-7
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = n
# y = 0
# reverse = -1 # 처음엔 x 감소시켜야

# limit = 0
# s = 1
# while s <= n*m:
#     for i in range(n - limit):   # 세로 채우기
#         x += reverse
#         # print(x, y)
#         board[x][y] = s
#         s+=1 
#     reverse *= -1

#     for i in range(m - limit -1):      # 가로 채우기
#         y += reverse
#         # print(x, y)
#         board[x][y] = s
#         s+=1     
#     limit += 1

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1491 : [기초-배열연습] 2차원 배열 달팽이 채우기 4-8
# n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]

# x = n
# y = 0
# reverse = -1 # 처음엔 x 감소시켜야

# limit = 0
# s = n*m
# while s >= 1:
#     for i in range(n - limit):   # 세로 채우기
#         x += reverse
#         # print(x, y)
#         board[x][y] = s
#         s-=1 
#     reverse *= -1

#     for i in range(m - limit -1):      # 가로 채우기
#         y += reverse
#         # print(x, y)
#         board[x][y] = s
#         s-=1     
#     limit += 1

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=" ")
#     print()

# 1492 : [기초-배열연습] 1차원 누적 합 배열 만들기 5-1
# n = int(input())
# nList = list(map(int, input().split()))
# for i in range(1, n+1):
#     s = 0
#     for j in range(i):
#         s += nList[j]
#     print(s, end=" ")

# 1493 : [기초-배열연습] 1차원 누적 합 배열 만들기 5-2
# 테스트 케이스 오류.
# n, m = map(int, input().split())
# # board = [[0]*m for i in range(n)]
# board = []
# sumboard = [[0]*m for i in range(n)]

# for i in range(n):
#     k = list(map(int, input().split()))
#     board.append(k)


# for i in range(n):
#     for j in range(m):

#         temp = 0
#         for ii in range(i+1):
#             for jj in range(j+1):
#                 temp += board[ii][jj]
#         sumboard[i][j] = temp

# for i in range(n):
#     for j in range(m):
#         print(sumboard[i][j], end=" ")
#     print()

# 1494 : [기초-배열연습] 1차원 차이 배열 만들기 5-3
# d[s] = d[s] + u
# d[e+1] = d[e+1] -u

# n, k = map(int, input().split())
# d = [0]*(n+1)
# for i in range(k):
#     s, e, u = map(int, input().split())
#     d[s-1] = d[s-1]+u
#     d[e] = d[e]-u

# for i in range(n):
#     print(d[i], end=" ")
# print()

# temp = 0
# for i in range(n):
#     temp += d[i]
#     d[i]= temp
#     print(d[i], end=" ")

22개 문제 풀지 않기로



