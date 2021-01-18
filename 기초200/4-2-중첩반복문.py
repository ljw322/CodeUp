# 1351 : 구구단 출력하기 2
# a, b = map(int, input().split())
# for i in range(a, b+1):
#     for j in range(1, 10):
#         print("%d*%d=%d"%(i, j, i*j))

# 1353 : 삼각형 출력하기 1
# n = int(input())
# for j in range(1, n+1):
#     print('*'*j)

# 1354 : 삼각형 출력하기 2
# n = int(input())
# for j in range(n, 0, -1):
#     print('*'*j)

# 355 : 삼각형 출력하기 3
# n = int(input())
# for j in range(n, 0, -1):
#     print(' '*(n-j)+'*'*j)

# 1357 : 삼각형 출력하기 4
# n = int(input())
# for i in range(1, n+1):
#     print('*'*i)
# for i in range(n-1, 0, -1):
#     print('*'*i)

# 1358 : 삼각형 출력하기 5
# n = int(input())
# for j in range(1, n+1, 2):  # 1 3 5 
#     print(' '*((n-j)//2) +'*'*j)

# for i in range(0, n//2+1):
#     print(' '*((n-1)//2 -i) + '*'*(i*2+1) + ' '*((n-1)//2 -i))

# 1352 : 사각형 출력하기 1
# n = int(input())
# for i in range(n):
#     print('*'*n)

# 1356 : 사각형 출력하기 2
# n = int(input())
# for i in range(n):
#     if i == 0 or i == n-1:
#         print('*'*n)
#     else: print('*'+' '*(n-2)+'*')

# 1365 : 사각형 출력하기 3
# n = int(input())
# for i in range(0, n):
#     for j in range(0, n):
#         if j == 0 or j == n-1 or i == 0 or i == n-1:
#             print('*', end="")
#         elif i == j or i+j+1==n:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()

# 1366 : 사각형 출력하기 4
# n = int(input())
# for i in range(0, n):
#     for j in range(0, n):
#         if j == 0 or j == n-1 or i == 0 or i == n-1:
#             print('*', end="")
#         elif i == j or i+j+1==n:
#             print('*', end="")
#         elif j == n//2 or i == n//2:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()

# 1367 : 평행사변형 출력하기 1
# n = int(input())
# for i in range(n, 0, -1):
#     print(' '*(i-1)+'*'*n)

# 1368 : 평행사변형 출력하기 2
# h, k, d = input().split()
# h = int(h)
# k = int(k)
# if d == 'R':
#     for i in range(h, 0, -1):
#         print(' '*(i-1) + '*'*k)
# else:
#     for i in range(h):
#         print(' '*(i) + '*'*k)

# 1361 : 별 계단 만들기
# n = int(input())
# for i in range(n):
#     print(' '*i+'**')

# 1369 : 빗금 친 사각형 출력하기
# n, k = map(int, input().split())
# for i in range(n): 
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1: print('*', end="")
#         elif (i+j)%k==k-1: print('*', end='')
#         else: print(' ', end="")
#     print()

# 1370 : 지그재그 출력하기
# h, r = map(int, input().split())
# for i in range(r):
#     for j in range(h):
#         print(' '*(j)+'*')
#     for j in range(h-1, 0, -1):
#         print(' '*(j-1)+'*')

# 1371 : 마름모 출력하기
# n = int(input())
# for i in range(1, n+1): #1부터 시작
#     print(' '*(n-i)+'*'+' '*(i-1)*2+"*")

# for i in range(n, 0, -1):
#     print(' '*(n-i)+'*'+' '*(i-1)*2+"*")

# 1378 : 수열의 합
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s+=i*(i+1)//2
# print(s)

# 1380 : 두 주사위의 합
# k = int(input())
# for i in range(1, k):
#     if i>6 or k-i>6: continue
#     else: print(i, k-i)

# 1382 : GuguClass
# for i in range(1, 10):
#     for j in range(2, 6):
#         print("%d x %d = %2d" %(j, i, j*i), end="")
#         if j != 5: print("\t", end="")
#     print()

# 1677 : 종이 자르기
a, b = map(int, input().split())
for i in range(b):
    if i == 0 or i == b-1:
        print('+'+'-'*(a-2)+'+')
    else:
        print('|'+' '*(a-2)+'|')
    print()
    
