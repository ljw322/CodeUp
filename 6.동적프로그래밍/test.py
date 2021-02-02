'''
1. selection sort
minIndex, loop x 2, swap

2. insertion sort
step by step to left

3. quick sort
array, start, end
recur(end condition), pivot, left, right, 

3-1. binary search (recursion)

3-2. binary search (loop)
'''
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = [0, 1, 2, 4, 5, 5, 6, 7, 8, 9]

def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target: return mid
        elif array[mid] < target: start = mid + 1
        else: end = mid -1

    return None

print(binarySearch(array, 5, 0, len(array)-1))




def quickSort(array, start, end):
    if start >= end: return

    pivot = start
    left = start + 1
    right = end

    while left <= end and array[pivot] >= array[left]:
        left += 1
    while start > right and array[pivot] <= array[right]:
        right -= 1
    if left > right:
        array[pivot], array[right] = array[right], array[pivot]
    else:
        array[left], array[right] = array[right], array[left]

    quickSort(array, start, right-1)
    quickSort(array, right+1, end)

quickSort(array, 0, len(array)-1)
print(array)

# def quickSort(array, start, end):
#     if start >= end: return

#     pivot = start
#     left = start+1
#     right = end
#     while left <= end and array[pivot] >= array[left]:
#         left += 1
#     while start > right and array[pivot] <= array[right]:
#         right -= 1
#     if left > right:
#         array[pivot], array[right] = array[right], array[pivot]
#     else:
#         array[left], array[right] = array[right], array[left]
    
#     quickSort(array, start, right-1)
#     quickSort(array, right+1, end)

# quickSort(array, 0, len(array)-1)
# print(array)



def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

# print('insertionSort:', insertionSort(array))

def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[minIndex] , array[i] = array[i], array[minIndex]

    return array

# print(selectionSort(array))