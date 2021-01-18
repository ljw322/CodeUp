# 1053 논리연산 1 -> 0, 0 -> 1
# n = int(input())
# n = bool(n)
# print(int(not n))
# print(not n)

# 1054 둘다 참일 때 참
# a, b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(int(a and b))

# 1055 하나라도 참이면 참
# a, b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(int(a or b))

# 1056 참,거짓 서로 다른때만 참 출력. 찌찌뽕은 0
# (1,0) (0,1) (1,1) (0,0)
# a, b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(int(a ^ b))

# 1057 참,거짓 서로 같을때만 참 출력.
# a, b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(int(not(a ^ b)))

# 1058 둘 다 거짓일 경우만 참 출력 (or의 반대)
# a, b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(int(not(a or b)))