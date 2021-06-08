# 21 06 04 17:20 ~ 17:35
'''
요약: 두 사람이 고를 수 있는 볼링공의 조합(단, 같은 무게 공 여러개. 다른것으로 취급)
해결: 볼링공 무게별 카운트 하고, 순열조합이용해 계산한다.
5 3
1 3 2 3 2
8 5
1 5 4 3 2 4 5 2
'''

n, m = map(int, input().split())

balls = list(map(int, input().split()))
info = [0]*(max(balls)+1)

balls.sort()

for value in balls:
    info[value] += 1

result = 0

for i in range(1, max(balls)):
    result += info[i]*(sum(info[i+1:]))


print(info)

print(result)