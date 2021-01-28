'''
계수정렬 - Count Sort O(N+K) K는 데이터 중 최대값
작은값과 큰값의 차이가 100만을 넘기지 않을때 good 
'''

array = [7, 5, 9, 0, 3, 1, 6, 4, 8]

count_array = [0] * (max(array)+1)

for i in array:
    count_array[i] += 1

for i in range(len(count_array)):
    if count_array[i] == 0: continue
    for j in range(count_array[i]):
        print(i, end=" ")