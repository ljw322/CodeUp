'''
예제4-1 상하좌우 시뮬레이션 문제
'''
n = int(input())
direction = list(input().split())

board = [[0]*(n+1) for i in range(n+1)]

x_point = [0, 0, -1, 1]
y_point = [-1, 1, 0, 0]
point = ['L', 'R', 'U', 'D']

x = 1
y = 1
for d in direction:

    for i in range(len(point)):
        if d == point[i]:
            x_Temp = x + x_point[i]
            y_Temp = y + y_point[i]

            if x_Temp < 1 or y_Temp < 1 or x_Temp > n or y_Temp > n:
                print(x_Temp, y_Temp, '무시')
            else:
                x += x_point[i]
                y += y_point[i]
                print(x, y)

print(x, y)
