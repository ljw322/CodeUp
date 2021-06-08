# 21 06 08 ...? 틀림
'''
요약: 먹방 시작 후 k초 후 넷웤장애. 몇 번 음식부터 섭취해야 하는가?(단, 음식 하나당 먹방1초, 주어진 순서대로 순환해서 먹음)
해결: 우선순위큐 이용. while ?? <= k일때, pop하면서 sumvalue, length, previous. 이후 번호순으로 정렬. (k-sum)%length출력
[8, 6, 4] -> 2
'''

import heapq

def solution(food_times, k):

    if k >= sum(food_times):
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sumvalue = 0
    previous = 0
    length = len(food_times)
    
    while sumvalue + (q[0][0]-previous)*length <= k:
        now = heapq.heappop(q)[0]
        sumvalue += (now-previous)*length
        length -= 1
        previous = now

    result = sorted(q, key = lambda x:x[1])
    return result[(k-sumvalue)%length][1]