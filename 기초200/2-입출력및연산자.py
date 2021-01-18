# 1110
# n = int(input())
# print(n)

# 1111
# n = input()
# print(n+"%")

# 1112
# a, b = input().split()
# print(a, b)

# 1113
# a, b = input().split()
# print(b, a)

# 1114, 1115
# a, b = input().split()
# print(int(a)+int(b))

# 1116
# a, b = input().split()
# a = int(a)
# b = int(b)
# print("%d+%d=%d" % (a, b, a+b))
# print("%d-%d=%d" % (a, b, a-b))
# print("%d*%d=%d" % (a, b, a*b))
# print("%d/%d=%d" % (a, b, a/b))

# 1117
# a, b = input().split()
# a = float(a)
# b = float(b)
# print("%.2f" % (a*b))

# 1118
# a, b = input().split()
# a = int(a)
# b = int(b)
# print("%.1f" % (a*b/2))

# 1119
# d = int(input())
# print(d*24)

# 1120
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# print("%.2f" % ((a+b+c)/3) )

# 1121
# a, b = input().split()
# a = int(a)
# b = int(b)
# print("%d" % (a%b) )

# 1122
# s = int(input())
# m = s // 60
# s = s % 60
# print(m, s)

# 1123
# f = int(input())
# c = 9/5*f+32
# print("%.3f" % c)

# 1125 8진수, 16진수 대문자 출력
# n = int(input())
# print("%o %X" %(n, n))

# 1126, 1132
# a = input()
# print(a)

# 1133
# n = input()
# print(n)

# 1135 관계
# a, b = map(int, input().split())
# print(int(a>=b))

# 1136 관계
# a, b = map(int, input().split())
# print(int(a==b))

# 1137 관계
# a, b = map(int, input().split())
# print(int(a!=b))

# 1138 논리 NOT
# a = int(input())
# print(int(not a))

# 1139 논리 AND
# a, b = map(int, input().split())
# print(int(a and b))

# 1140 논리 OR
# a, b = map(int, input().split())
# print(int(a or b))

# 1143 비트 AND
# a, b = map(int, input().split())
# print(a & b)

# 1144 비트 OR
# a, b = map(int, input().split())
# print(a | b)

# 1147
# a, x = map(int, input().split())
# print(a<<x)

# 1148
# a, x = map(int, input().split())
# print(a>>x)

# 1149
# a, b = map(int, input().split())
# print(a if a>=b else b)

# 1150
a, b, c = map(int, input().split())
m = b if a>=b else a
print(m if c>=m else c)



