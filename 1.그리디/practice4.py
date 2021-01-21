'''
#04 만들 수 없는 금액 15:00 ~ 15:30 제한시간 1초
input 5
      3 2 1 1 9
output 8
1 2 3 4 5 6 7 9 10 11 12

input 3
      3 5 7
output 1
3 5 7 8 10 12

조합으로 모든 경우의 합을 정렬하여 품.. 
-> 1부터 차례대로 특정 금액을 만들 수 있는지 확인!! & target값 증가update
'''
import time

start_time = time.time()

# from itertools import combinations
# n = int(input())
# arr = list(map(int, input().split()))
# sumSet = set()

# combi = []
# for i in range(1, len(arr)+1):
#     combi.append(list(combinations(arr, i)))

# for i in combi:
#     for j in i:
#         sumSet.add(sum(j))

# end = list(sumSet)[-1]
# i = 1
# while i <= end:
#     if i == list(sumSet)[i-1]: pass
#     else: break
#     i+=1
# print(i)

# end_time = time.time()
# print("프로그램 수행시간: ", end_time - start_time)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for _ in arr:
    if target < _:  # 만들 수 없는 금액을 찾을 때 반복 종료
        break
    else:
        target+=_   # target update
print(target)

end_time = time.time()
print("프로그램 수행시간: ", end_time - start_time)