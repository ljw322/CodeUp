'''
숫자카드게임 2021-01-18 17:04 ~ 17:34
행 선택 후, 가장 낮은 수를 선택해야 한다.
행별로 가장 낮은것들 리스트에 담고 젤 큰거
'''
n, m = map(int, input().split())
# board = [[0]*m for i in range(n)]
board = []
eachMin = []
for i in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    arr.sort()
    eachMin.append(arr[0])

eachMin.sort()
print(eachMin[-1])
