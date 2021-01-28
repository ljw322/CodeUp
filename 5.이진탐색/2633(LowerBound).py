'''
2633 Lower Bound
정렬되어있는 n개의 수에서
k이상인 수가 처음으로 등장하는 위치는?
'''
n, k = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(array, target, start, end):
    # if start > end: return None

    while start < end:
        mid = (start+end) // 2

        if array[mid] >= target: end = mid
        else: start = mid + 1

    return end

result = binarySearch(array, k, 0, len(array)-1)

if array[result] < k : print(n+1)
else: print(result+1)


