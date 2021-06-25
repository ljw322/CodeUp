# 21 05 13 16:50 ~ 17:10

n = int(input())
infoList = []

for i in range(n):
    name, a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(b)
    infoList.append([name, a, b, c])

infoList.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for _ in infoList:
    print(_[0])