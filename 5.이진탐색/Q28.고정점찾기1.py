# 21 05 16 16:15 ~ 35(20분)


'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''
n = int(input())
nList = list(map(int, input().split()))

def binarySearch(array, start, end):

    while start <= end:
        mid = (start+end)//2

        if mid == array[mid]: return mid
        if mid < array[mid]: end = mid-1
        else: start = mid+1

    return -1

result = -1
result = binarySearch(nList, 0, n-1)
# for value in nList:
#     result = binarySearch(nList, value, 0, n-1)
    
#     if result != -1:
#         print(result)
#         break

# if result == -1: print(-1)

print(result)