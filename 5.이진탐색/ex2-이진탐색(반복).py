'''
2. binary search loop  (array, target, start, end)
- while end condition, mid, target
- 2 times return
'''

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binarySearchLoop(array, target, start, end):
    while start <= end:

        mid = (start+end)//2

        if array[mid] == target: return mid
        elif target < array[mid]: end = mid -1
        else: start = mid + 1

    return None

print(binarySearchLoop(array, 9, 0, len(array)-1))