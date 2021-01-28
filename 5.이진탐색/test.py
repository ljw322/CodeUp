'''
1. selection sort
minIndex, loop x 2, swap

2. insertion sort
step by step to left

3. quick sort
array, start, end
recur(end condition), pivot, left, right, 
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array, start, end):
    if start >= end: return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] <= array[right]:
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

#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while start < right and array[pivot] <= array[right]:
#             right -= 1
#         if left > right: # 엇갈린다면
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
#     quickSort(array, start, right-1)
#     quickSort(array, right+1, end)
    
#     return array
# quickSort(array, 0, len(array)-1)
# print(array)


# def quickSort(array, start, end):
#     if start >= end: return

#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right:
#         # left == find big data
#         while left <= end and array[left] <= array[pivot]:  
#             left += 1
#         # right == find small data
#         while start < right and array[pivot] <= array[right]:   
#             right -= 1
#         # if cross, change pivot value and small data
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot] 
#         # if not cross, change small and big data
#         else:
#             array[left], array[right] = array[right], array[left] 

#     # go recursion
#     quickSort(array, start, right-1)
#     quickSort(array, right+1, end)

# quickSort(array, 0, len(array)-1)
# print(array)

def insertionSort(array):
    for i in range(1, len(array)):
          # 0 번째 인덱스는 정렬되어있다고 가정이므로 (i, 0, -1)
        for j in range(i, 0, -1): 
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    print(array)

def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    print(array)

# selectionSort(array)
# insertionSort(array)