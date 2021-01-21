'''
#05 볼링공 고르기 15:55 ~ 16:25 제한시간 1초
두 사람이 볼링공을 고르는 경우의 수는? 시간초과 3초나옴.
'''
from itertools import combinations
import time

start_time = time.time()

n, m = map(int, input().split())
ball = list(map(int, input().split()))

balls = list(combinations(ball, 2))
# print(balls)

count = 0
for x in balls:
    if x[0] == x[1]: count+=1
    
# print(count)
print(len(balls) - count)

# array = [0]*11
# for x in ball:
#     array[x] += 1

# result = 0
# for i in range(1, m+1):
#     n-=array[i]
#     result += array[i]*n
# print(result)

end_time = time.time()
print("프로그램 수행시간: ", end_time - start_time)



