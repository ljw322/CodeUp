# 2021 04 11 13:20 ~ 13:
'''
4
5 1 7 9

4
1 1 1 1
'''

n = int(input())
houses = list(map(int, input().split()))

houses.sort()

print(houses[(n-1)//2])