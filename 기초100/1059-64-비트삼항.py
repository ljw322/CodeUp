# 1059 비트단위 NOT
# n = int(input())
# print(~n)

# 1060 비트단위 AND
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a & b)

# 1061 비트단위 OR
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a | b)

# 1062 비트단위 XOR
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a ^ b)

# 1063 두 정수 중 큰 수는? 삼항연산 이용하기
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a if a >= b else b)

# 1063 세  정수 중 작은 수는? one-liner
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
m = a if a <= b else b
print(m if m <= c else c)
