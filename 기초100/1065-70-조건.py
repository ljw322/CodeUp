# 1065 짝수만 출력
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

# result = [];
# if a % 2 == 0:
#     result.append(a)
# if b % 2 == 0:
#     result.append(b)
# if c % 2 == 0:
#     result.append(c)

# for _ in result:
#     print(_)

# 1066 짝홀 출력하기
# result = input().split()

# for _ in result:
#     if int(_) % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# 1067 부호,짝홀 출력하기
# n = int(input())
# print('plus' if n > 0 else 'minus')
# print('even' if n % 2 == 0 else 'odd')

# 1068 점수 평가하기
# n = int(input())

# if 90 <= n <= 100: r = 'A'
# elif 70 <= n <= 89: r = 'B'
# elif 40 <= n <= 69: r = 'C'
# else: r = 'D'

# print(r)

# 1069 평가 출력 다르게하기
# n = input()

# if n == 'A': r = 'best!!!'
# elif n == 'B': r = 'good!!'
# elif n == 'C': r = 'run!'
# elif n == 'D': r = 'slowly~'
# else: r = 'what?'

# print(r)

# 1070 달에 따른 계절 출력토록
n = int(input())
if n == 12 or n == 1 or n == 2: r = 'winter'
elif n == 3 or n == 4 or n == 5: r = 'spring'
elif n == 6 or n == 7 or n == 8: r = 'summer'
else: r = 'fall'

print(r)
