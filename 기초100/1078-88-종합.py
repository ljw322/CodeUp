# 1078 짝수 합 구하기
# n = int(input())

# sum = 0
# for _ in range(n+1):
#     if _ % 2 == 0 :
#         sum += _

# print(sum)

# 1079 q가 입력될 때까지 입력된 문자 출력
# inputVal = input().split()

# for _ in inputVal:
#     print(_)
#     if _ == 'q':
#         break
    
# 1080 
# n = int(input())

# sum = 0
# i = 0
# while sum < n:
#     i += 1
#     sum += i
    
# print(i)

# 1081 주사위 두 개를 던지면?
# a, b = input().split()
# a = int(a)
# b = int(b)

# for n in range(1, a+1):
#     for m in range(1, b+1):
#         print(n, m)

# 1082 16진수 구구단?
# 16진수 -> 10진수 
# a = int(input(), 16)

# for _ in range(1, 16):
#     print("%X*%X=%X" %(a, _, a*_) )

# 1083
# n = int(input())

# for _ in range(1, n+1):
#     if _ % 3 == 0:
#         print('X', end=' ')
#     else:
#         print(_, end=' ')

# 1084 빛 섞어 색 만들기
# r, g, b = input().split()
# r = int(r)
# g = int(g)
# b = int(b)
# c = 0
# for i in range(r):
#     for j in range (g):
#         for k in range (b):
#             print(i, j, k)
#             c+=1

# print(c)

# 1085 소리 파일 저장용량 계산하기
# h, b, c, s = input().split()
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)

# bit = h * b * c * s
# byte = bit / 8
# kbyte = byte / 1024
# mbyte = kbyte / 1024

# print(round(mbyte,1), "MB")

# 1086 그림 파일 저장용량 계산하기
# w, h, b = input().split()
# w = int(w)
# h = int(h)
# b = int(b)

# bit = w * h * b
# byte = bit / 8
# kbyte = byte / 1024
# mbyte = kbyte / 1024

# print("%.2f MB" % round(mbyte,2))

# 1087 여기까지! 이제 그만 ~
# n = int(input())

# i = 1
# sum = 1
# while sum < n :
#     i += 1
#     sum += i

# print(sum)

# 1088 3의 배수는 통과
n = int(input())

for _ in range (1, n+1):
    if _ % 3 == 0: continue
    print(_, end=" ")