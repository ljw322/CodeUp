# 2021 04 11 12:20 ~ 12:35 
'''
3
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
파이썬 sort로 해결가능한 부분이다.
'''
n = int(input())
info = []

for i in range(n):
    # scores = list(input().split(" "))
    scores = input().split()
    info.append(scores)

info.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(info[i][0])