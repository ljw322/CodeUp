'''
퀵정렬 - Quick Sort O(NlogN)
피벗, 왼쪽, 오른쪽, 재귀
거의 정렬되어 있을 수록 시간은 그닥
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
     # 종료 조건
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))