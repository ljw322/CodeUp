'''
예제 4-2 시각 완전탐색 유형
N시 59분 59초 까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하라
하루는 86400초. 24시 -> 24*60분 -> 24*60*60초 10만 개도 되지 않음
파이썬, 1초에 2000만번의 수행을 한다
시,분,초 3중 반복문을 이용해 풀 수 있다.
'''
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)