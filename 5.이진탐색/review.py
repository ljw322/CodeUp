'''
# 떡볶이 떡 만들기
# 적어도 m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값?
4 6
19 15 10 17
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = 0

start = 0
end = max(array)

def binarySearch(array, target, start, end):

    while start <= end:

        mid = (start+end)//2
        sumTemp = 0

        for x in array:
            if x > mid:
                sumTemp += x - mid

        if sumTemp >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(binarySearch(array, m, 0, end))
