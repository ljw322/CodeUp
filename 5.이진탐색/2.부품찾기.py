'''
2. 부품찾기 30분 1초 128MB ~ 16:00
=> 이진탐색 loop형식 쓰는 과정에서 틀림
=> list대신 set으로 데이터를 입력받아 풀 수도 있다.
5
8 3 7 9 2
3
5 7 9
'''
n = int(input())
goods = list(map(int, input().split()))
goods.sort()

m = int(input())
buyList = list(map(int, input().split()))

def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target: return 'yes'
        elif target < arr[mid]: end = mid - 1
        else: start = mid + 1

    return 'no'

for x in buyList:
    print(binarySearch(goods, x, 0, len(goods)-1), end=" ")

