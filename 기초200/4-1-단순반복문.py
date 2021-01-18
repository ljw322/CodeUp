# 1251 1-100까지 출력
# for _ in range(1, 101):
#     print(_, end=" ")

# 1252 1부터 n까지 출력
# n = int(input())
# for _ in range(1, n+1):
#     print(_, end=" ")

# 1253 a부터 b까지 출력
# a, b = map(int, input().split())
# if a > b:
#     temp = b
#     b = a
#     a = temp
# for _ in range(a, b+1):
#     print(_, end=" ")

# 1254 알파벳 출력하기
# a, b = input().split()
# for _ in range(ord(a), ord(b)+1):
#     print(chr(_), end=" ")

# 1255 두 실수 사이 출력하기
# a, b = map(float, input().split())

# while (a < b):
#     print("%.2f"% round(a, 2), end=" ")
#     a += 0.01

# if a == b: print(a)

# 1256 별 찍기
# n = int(input())
# for _ in range(n):
#     print("*", end="")

# 1257 두 수 사이 홀수 출력
# a, b = map(int, input().split())

# for _ in range(a, b+1):
#     if _%2 == 1: print(_, end=" ")

# 1258 1부터 n까지 합 구하기
# n = int(input())
# sum = 0
# for _ in range(n+1):
#     sum+=_
# print(sum)

# 1259 1부터 n까지 중 짝수 합
# n = int(input())
# sum = 0
# for _ in range(n+1):
#     if _%2 == 0: sum+=_
# print(sum)

# 1260 3의 배수의 합 
# a, b = map(int, input().split())
# sum = 0
# for _ in range(a, b+1):
#     if _ % 3 == 0: sum += _
# print(sum)

# 1261 First Special Judge (Test)
# value = list(map(int, input().split()))
# for _ in value:
#     if _ % 5 == 0:
#         print(_)
#         break
#     elif _ % 5 != 0 and _ == value[-1]:
#         print(0)

# 1265 구구단 출력
# n = int(input())

# for _ in range(1,10):
#     print("%d*%d=%d" %(n, _, n*_))

# 1266 n개의 수의 합
# n = int(input())
# value = list(map(int, input().split()))

# sum = 0
# for _ in value:
#     sum += _
# print(sum)

# 1267 : n개의 수 중 5의 배수의 합
# n = int(input())
# value = list(map(int, input().split()))

# sum = 0
# for _ in value:
#     if _ % 5 == 0: sum += _
# print(sum)

# 1268 : n개의 수 중 짝수의 개수
# n = int(input())
# value = list(map(int, input().split()))

# count = 0
# for _ in value:
#     if _ % 2 == 0: count+=1
# print(count)

# 1269 : 수열의 값 구하기
# a, b, c, n = map(int, input().split())
# for _ in range(n-1):
#     a = a * b + c
#     # print(a)
# print(a)

# 1270 : 1의 개수는? 1
# n = int(input())
# count = 0
# for _ in range(1, n+1):
#     if (str(_)[-1]=='1'): count+=1
# print(count)

# 1271 : 최대값 구하기
# n = int(input())
# value = list(map(int, input().split()))
# value.sort()
# print(value[-1])

# 1272 : 기부
# k, h = map(int, input().split())
# def money(n):
#     if n % 2 == 0: return n/2*10
#     else: return (n+1)/2

# print(int(money(k)+money(h)))

# 1273 : 약수 구하기
# n = int(input())
# for _ in range(1, n+1):
#     if n%_==0: print(_, end=" ")

# 1274 : 소수 판별
# def getCount(n):
#     count = 0
#     for _ in range(1, n+1):
#         if n%_==0: count+=1
    
#     if count == 2: return "prime"
#     else: return "not prime"


# n = int(input())
# print(getCount(n))


# 1275 : k 제곱 구하기
# n, k = map(int, input().split())
# print(n**k)

# 1276 : 팩토리얼 계산
# n = int(input())
# pacto = 1
# for _ in range(1, n+1):
#     pacto *= _

# print(pacto)


# 1277 : 몇 번째 데이터 출력하기
# n = int(input())
# value = list(map(int, input().split()))
# print(value[0], value[n//2], value[-1])

# 1278 : 자릿수 계산
# n = input()
# print(len(n))

# 1279 : 홀수는 더하고 짝수는 빼고 1
# a, b = map(int, input().split())
# sum = 0
# for _ in range(a, b+1):
#     if _ % 2 != 0: sum += _
#     else: sum -= _
# print(sum)

# 1280 : 홀수는 더하고 짝수는 빼고 2
# a, b = map(int, input().split())
# sumVal = 0
# sen = ""
# for _ in range(a, b+1):
#     if _ % 2 != 0:
#         sumVal += _
#         sen += "+"+str(_)
#     else:
#         sumVal -= _
#         sen += "-"+str(_)
# sen += "="+str(sumVal)
# print(sen)

# 1281 : 홀수는 더하고 짝수는 빼고 3
# 불필요한 '+'만 빼는 것임. -는 첫 순서여도 표시함
# a, b = map(int, input().split())
# sumVal = 0
# sen = ""
# for _ in range(a, b+1):
#     if _ % 2 != 0:
#         sumVal += _
#         sen += "+"+str(_)
#     else:
#         sumVal -= _
#         sen += "-"+str(_)

# sen += "="+str(sumVal)
# if sen[0] == '+': print(sen[1:])
# else: print(sen)

# 1282 : 제곱수 만들기 n-k(k는 젤 작은)
# 처음에 생각했었던 방법. 블로그 참조함. 
# import math
# n = int(input())
# k = 0
# for _ in range(1, n):
#     if math.sqrt(n-_) % 1 == 0:
#         print(_, int(math.sqrt(n-1)))
#         break


# 시간초과!!2
# n = int(input())
# listVal = []
# for _ in range(1, n//2+1):
#     if _*_<= n:
#         listVal.append(_)
# print(n-listVal[-1]*listVal[-1], listVal[-1])

# 시간초과!!1
# k = 0
# value = 0
# check = 0
# for _ in range(1, n):
#     k = n-_
#     for i in range(1, k+1):
#         if i*i==k:
#             print(_, i)
#             check = 1
#             break
#     if check == 1:break

# 1283 : 주식 투자
# a = int(input())
# initPrice = a
# b = int(input())
# info = list(map(int, input().split()))
# for _ in info:
#     a = a + a*(_/100)

# compare = a - initPrice #순수익 = 총 수익 - 투자금액
# compare = int(round(compare, 0))

# print(compare)
# if compare < 0: print('bad')
# elif compare > 0: print('good')
# else: print('same')

# 1284 : 암호 해독 -> 두 소수의 곱으로 나타내기
# def CheckNum(n):
#     count = 0
#     for _ in range(1, n+1):
#         if n%_==0: count+=1
    
#     if count == 2: return 1
#     else: return 0


# n = int(input())

# a = 0
# b = 0
# for _ in range(2, n//2+1):
#     if CheckNum(_) == 1 and n%_==0 and CheckNum(n//_)==1:
#         a = _
#         b = n//_
#         break

# if a == 0: print("wrong number")
# else: print(a, b)




# 1285 : 계산기 2
# sen = input()
# numList = []
# operList = []

# start_point = 0
# end_point = 0
# for _ in sen:
#     if _ == '+' or _ == '-' or _ == '*' or _ == '/' or _ == '=':
#         numList.append(int(sen[start_point:end_point]))
#         operList.append(sen[end_point:end_point+1])
#         start_point = end_point+1

#     end_point += 1

# # print(numList)
# # print(operList)

# a = numList[0]
# for i in range(len(operList)-1):
#     if operList[i] == '+':
#         a += numList[i+1]
#     elif operList[i] == '-':
#         a -= numList[i+1]
#     elif operList[i] == '*':
#         a *= numList[i+1]
#     elif operList[i] == '/':
#         a = int(a/numList[i+1])
    
# print(int(a))


# 1286 : 최댓값, 최솟값
# arr = []
# for _ in range(5):
#     n = int(input())
#     arr.append(n)
# arr.sort()
# print(arr[-1])
# print(arr[0])

# 1287 : 구구단을 *로 출력하기
# n = int(input())
# for i in range(1, 10):
#     print('*'*(n*i))

# 1675 : 시저의 암호 1 암호->평문
# chiper = input()
# original = []
# for _ in chiper:
#     if _ == " ":
#         original.append(" ")
#     elif _ == 'a':
#         original.append('x')
#     elif _ == 'b':
#         original.append('y')
#     elif _ == 'c':
#         original.append('z')
#     else:
#         original.append(chr(ord(_)-3))
# for _ in original:
#     print(_, end="")


# 1294 : 시저의 암호 2 평문->암호
# original = input()
# chiper = []
# for _ in original:
#     if _ == " ":
#         chiper.append(" ")
#     elif _ == 'x':
#         chiper.append('a')
#     elif _ == 'y':
#         chiper.append('b')
#     elif _ == 'z':
#         chiper.append('c')
#     else:
#         chiper.append(chr(ord(_)+3))
# for _ in chiper:
#     print(_, end="")

# 1295 : 알파벳 대소문자 변환
print(ord('a'), ord('z'), ord('A'), ord('Z'))
n = input()
for _ in n:
    if 97<=ord(_)<=122: print(str.upper(_), end="")
    elif 65<=ord(_)<=90: print(str.lower(_), end="")
    else: print(_, end="")



