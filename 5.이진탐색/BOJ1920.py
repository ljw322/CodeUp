'''
1920 수 찾기
'''
n = int(input())
array = list(map(int, input().split()))
m = int(input())
tofind = list(map(int, input().split()))

array.sort()

def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if array[mid] == target: return 1
        elif array[mid] > target: end = mid -1
        else: start = mid + 1

    return 0

for x in tofind:
    print(binarySearch(array, x, 0, len(array)-1))
