'''
3. 떡볶이 떡 만들기 40분 2초 128MB ~ 16:30
4 6
19 15 10 17
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binarSearch(arr, m, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in arr:
            if x > mid:
                total += x - mid

        if total >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1            
    
    return result

print(binarSearch(arr, m, 0, arr[-1]))