# 1071, 1073 0입력되면 종료
# inputList = input().split()
# for _ in inputList:
#     if int(_) != 0:
#         print(_)
#     else:
#         break

# 1072 정수 계속 출력
# n = int(input())
# listVal = input().split()

# for _ in listVal:
#     print(_)

# 1074 카운트다운1
# n = int(input())

# while n > 0:
#     print(n)
#     n-=1

# 1075 카운트다운2
# n = int(input())

# n -= 1
# while n >= 0:
#     print(n)
#     n-=1

# 1076 a부터 그 알파벳까지 출력하기
# n = input()
# start = ord('a')
# end = ord(n)

# while start <= end:
#     print(chr(start), end=' ')
#     start += 1

# 1077 0부터 그 수 까지 출력하기
n = int(input())

for _ in range(n+1):
    print(_)
    