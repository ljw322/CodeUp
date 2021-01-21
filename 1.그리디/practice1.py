'''
2021-01-21 #01 모험가 길드 11:20 ~ 11:50 
여행을 떠날 수 있는 그룹 수의 최댓값
최대값을 구해야 하므로. 낮은 수 부터 그룹을 묶어야 한다..!!! 내림차순이 아님.
5
2 3 1 2 2

1 2 2 2 3
0 1 2 3 4
'''
# n = int(input())
# fear = list(map(int, input().split()))
# fear.sort()

# count = 0
# i = 0
# while i <= len(fear):
#     start = i
#     i += fear[i]
#     end = i
#     if end >= len(fear): break
#     minVal = fear[start]
#     flag = 0
#     for k in range(start+1, end):        
#         if minVal < fear[k]:
#             flag = 1
#             break
#     if flag == 0: count += 1
    

# print(count)

# print("start:", start, "end:", end,)
# print("minVal:", minVal, "fear[k]:", fear[k])
# print("count: ", count)

'''
더 간단한 풀이
'''
n = int(input())
fear = list(map(int, input().split()))
fear.sort()

result = 0
count = 0

for i in fear:
    count+=1
    print("i:", i, "count:", count)
    if count >= i:
        result += 1
        count = 0
print(result)