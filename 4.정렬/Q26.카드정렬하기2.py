# 21 05 16 14:35 ~ 15:00 (30분)
import heapq

n = int(input())
heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))

answer = 0

# 길이가 1일때까지.
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum_value = a + b
    answer += sum_value
    heapq.heappush(heap, sum_value)

print(answer)