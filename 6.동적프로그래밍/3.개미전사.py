'''
3. 개미전사
최대한 많은 식량을 얻기 위한 식량의 최대값.
메뚜기 병사 서로 인접한 식량창고가 공격받으면 바로 알 수 있어
bottom up
a(i) = max(a(i-1), a(i-2) + k(i))
'''
n = int(input())
foodList = list(map(int, input().split()))

a = [0] * 101
a[0] = foodList[0]
a[1] = max(foodList[0], foodList[1])

for i in range(2, n):
    a[i] = max(a[i-1], a[i-2]+foodList[i])

print(a[n-1])

