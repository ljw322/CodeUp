'''
2. 왕실의 나이트 풀이시간 20분 시간제한 1초 메모리 128MB 14:10 ~ 14:30
나이트가 움직여 갈 수 있는 곳의 경우의 수
'''

position = input()
x = ord(position[0]) - 96
y = int(position[1])
# print(x, y)

x_dict = [-1, 1, 2, 2, 1, -1, -2, -2]
y_dict = [-2, -2, -1, 1, 2, 2, 1, 1]

count = 0
for i in range(8):
    x_temp = x + x_dict[i]
    y_temp = y + y_dict[i]
    if x_temp < 1 or y_temp < 1 or x_temp > 8 or y_temp > 8:
        continue
    count += 1

print(count)