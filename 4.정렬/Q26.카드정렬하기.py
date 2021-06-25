# 2021 04 11 16:10 ~ 40
'''
heapq를 이용한다.
3
10
20
40
'''
import heapq

n = int(input())
heap = []

# heapq에 데이터 넣기. 자동정렬. (우선순위 큐)
for i in range(n):
    dummy = int(input())
    heapq.heappush(heap, dummy)

result = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    sumvalue = a + b
    result += sumvalue
    heapq.heappush(heap, sumvalue)

print(result)

