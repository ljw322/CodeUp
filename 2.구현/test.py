# 1. 상하좌우
# n = int(input())
# plan = list(input().split())

# # LRUD
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# x = 1
# y = 1
# for direction in plan:
#     if direction == 'L':
#         nx = x + dx[0]
#         ny = y + dy[0]
#     elif direction == 'R':
#         nx = x + dx[1]
#         ny = y + dy[1]
#     elif direction == 'U':
#         nx = x + dx[2]
#         ny = y + dy[2]
#     else:
#         nx = x + dx[3]
#         ny = y + dy[3]
    
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     else:
#         x, y = nx, ny
# print(x, y)

#2. 시각
# n = int(input())

# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             time = str(i)+str(j)+str(k)
#             for _ in time:
#                 if _ == '3':
#                     count += 1
#                     break
# print(count)

# 2. 

# position = input()

# x = ord(position[0]) -97 + 1
# y = int(position[1])

# dx = [-2, -1, 1, 2, 2, 1, -1, -2]
# dy = [1, 2, 2, 1, -1, -2, -2, -1]

# count = 0
# for i in range(8):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     else: count += 1

# print(count)


#3 게임개발









