'''
#05 볼링공 고르기 15:55 ~ 16:25 제한시간 1초
두 사람이 볼링공을 고르는 경우의 수는? 시간초과 3초나옴.
combination은 메모리 초과로 이어질 수 있다.
경우의 수로 풀자. 각 무게별로 공이 몇개있는지 파악한다.
'''
# from itertools import combinations
import time
start_time = time.time()

n, m = map(int, input().split())
ballList = [0]*(n+1)

ball = list(map(int, input().split()))
for _ in ball:
    ballList[_] += 1

untilcount = 0
case = 0
ball_weight = 1

for i in range(1, n+1):
    if ballList[i] == 0 : continue

    untilcount += ballList[i]
    case += ballList[i] * (n-untilcount)
    ball_weight += 1

print(case)

# balls = list(combinations(ball, 2))
# print(balls)

# count = 0
# for x in balls:
#     if x[0] == x[1]: count+=1
    
# # print(count)
# print(len(balls) - count)



end_time = time.time()
print("프로그램 수행시간: ", end_time - start_time)



