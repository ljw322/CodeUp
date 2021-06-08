# 21 06 07 15:15 ~ 15:42
'''
요약: 사람별 공포도가 주어질 때, 여행떠날수있는 그룹의 최대값
해결: 내림차순아닌 오름차순, 큐이용함
5
2 3 1 2 2
6
2 3 1 2 2 1
'''
from collections import deque

n = int(input())

nList = list(map(int, input().split()))
nList.sort()

q = deque()
for value in nList:
    q.append(value)

count = 0
while q:
    n = q[0]
    flag = True

    for i in range(n):
        value = q.popleft()
        if value > n:
            flag = False
    if flag == True:
        count += 1
    
print(count)