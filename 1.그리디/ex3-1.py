# 거스름돈
# 거슬러 줘야 할 동전의 최소 개수는?
# 500, 100, 50, 10원
n = int(input())
coin = [500, 100, 50, 10]

count = 0
r = 0

for _ in coin:
    count += n // _
    n %= _

print(count)



