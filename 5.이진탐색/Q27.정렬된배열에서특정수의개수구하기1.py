# 21 05 16 15:33 ~ 16:00 (30분)
# 두가지 풀이법(직접구현, 라이브러리 이용)
'''
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
'''
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nList = list(map(int, input().split()))
print(nList)

a = bisect_left(nList, x)
b = bisect_right(nList, x)
# print(a, b)

if b-a == 0: print(-1)
else: print(b-a)
# def getminIndex(array, target, start, end):
    
#     index = -1
#     while start <= end:
#         midIndex = (start+end)//2

#         if target <= array[midIndex]:
#             if target == array[midIndex]:
#                 index = midIndex
#             end = midIndex-1
            
#         else:
#             start = midIndex+1

#     return index

# def getmaxIndex(array, target, start, end):
    
#     index = -1
#     while start <= end:
#         midIndex = (start+end)//2

#         if target >= array[midIndex]:
#             if target == array[midIndex]:
#                 index = midIndex
#             start = midIndex+1
#         else:
#             end = midIndex-1

#     return index


# a = getminIndex(nList, x, 0, n-1)
# b = getmaxIndex(nList, x, 0, n-1)
# # print(a, b)

# if a == -1 or b == -1:
#     print(-1)
# else: 
#     print(b-a+1)
