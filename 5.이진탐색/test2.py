# 2. 부품 찾기
# 3. 떡볶이 떡 만들기
'''
4 6
19 15 10 17
'''
n, target = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = arr[-1]

height = 0  #절단기 최대 높이 저장
while start <= end:
    mid = (start+end) // 2

    sumValue = 0
    for _ in arr:
        if _ > mid:
            sumValue += _ - mid

    if sumValue >= target:
        height =  mid
        start = mid+1
    else:
        end = mid-1

print(height)