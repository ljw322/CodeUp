# 예제2번. 큰 수의 법칙 2021.01.18 13:59~16:29
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# 가장큰 수 두개를 뽑으면서
# 가장큰수 k번 더한 후, 그 다음으로 작은 수 한번 더함
# arr.sort()
# arr.reverse()

# a = arr[0]
# b = arr[1]

# i = 1
# count = 1
# res = 0
# while i <= m:
#     if count % k == 0:
#         res += b
#         count = 1
#     else:
#         res += a
#         count += 1
#     i += 1       

# print(res)

'''
--> 정답!
그런데 m이 100억 이사일 때 시간 초과 날 수 있다.
좀 더 효율적인 방법 중 하나로 반복되는 수열 파악해보자
5 8 3 (n, m, k)
2 4 5 4 6
위 input에 대한 출력반복은 666566656665...
가장 큰수가 더해지는 횟수는 int(m/(k+1))*k + m%(k+1)
'''
arr.sort()
a = arr[-1]
b = arr[-2]

count = int(m/(k+1))*k
count += m % (k+1)

res = 0
res += a * count
res += b * (m-count)

print(res)