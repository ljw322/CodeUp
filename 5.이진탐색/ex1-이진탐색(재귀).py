'''
1. binary search recursion
array, target, start, end
end condition, mid(index!)
find, if target small, if target big
4 times return
'''

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binarySearch(array, target, start, end):
    if start > end: return None

    mid = (start+end) // 2

    if array[mid] == target: return mid

    elif target < array[mid]:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)

print(binarySearch(array, 20, 0, len(array)-1))