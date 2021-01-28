'''
삽입정렬 - Insertion Sort O(N^2) 최선의 경우 O(N)
필요 시만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적 (퀵보다 빨라)
그 앞의 데이터들은 이미 정렬되어 있다!
자기 자신보다 작은 데이터를 만날 때 삽입한다.
0 5 7 9 | 3 1 6 2 4 8
(3은 '왼쪽'으로 swap하면서 자기보다 작은 0을 만나고 멈춘다.)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)