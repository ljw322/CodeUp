#  1089 등차수열 계산
# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)

# for _ in range(n-1):
#     a += d

# print(a)

# 1090 등비수열 계산
# a, r, n = input().split()
# a = int(a)
# r = int(r)
# n = int(n)

# for _ in range(n-1):
#     a *= r

# print(a)

# 1091 수열 계산 3
# a, m, d, n = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)

# for _ in range(n-1):
#     a = a * m + d

# print(a)

# 1092 함께 문제 푸는 날
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# day = 1
# while day % a != 0 or day % b != 0 or day % c != 0:
#     day += 1
# print(day)

# 1093 이상한 출첵1
# n = int(input())
# inputVal = input().split()

# listVal = [0] * 23

# for _ in inputVal:
#     listVal[int(_)-1] += 1

# for _ in listVal:
#     print(_, end=" ")

# 1094 이상한 출첵2
# n = int(input())
# arr = input().split()
# arr.reverse()

# for _ in arr:
#     print(_, end=" ")

# 1095 이상한 출첵3
n = int(input())
arr = input().split()
arr = list(map(int, arr))
arr.sort()
print(arr[0])


