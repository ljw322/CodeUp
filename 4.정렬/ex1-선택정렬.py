'''
선택정렬 - Selection Sort O(N^2)
가장 작은 데이터를 찾아서 swap
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 0번 인덱스부터 진행
for i in range(len(array)):
    minIndex = i
    # minIndex 찾기 i+1부터~
    for j in range(i+1, len(array)):
        if array[minIndex] > array[j]:
            minIndex = j
    array[i], array[minIndex] =  array[minIndex], array[i]

print(array)