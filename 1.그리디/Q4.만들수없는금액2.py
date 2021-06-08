# 21 06 07 16:35 ~ 16:50
'''
요약: N개의 동전을 이용하여 만들 수 없는 양의 정수 최솟값을 구해라.
해결: 1. combination을 이용하면 시간, 메모리 초과가 날 확률이 높다.
      2. 오름차순정렬. 1부터 차례대로 특정금액을 만들 수 있는지 확인.
         target금액을 만들 수 있다면(target>=value), target금액을 update한다.
5
3 2 1 1 9
'''
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for value in coins:
    
    if target >= value:
        target += value
    else:
        break
print(target)



# from itertools import combinations

# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()

# kinds = set()

# for i in range(1,n+1):
#     temp = list(combinations(coins, i))
#     for value in temp:
#         kinds.add(sum(value))

# for i in range(1, sum(coins)+1):
#     if i not in kinds:
#         print(i)