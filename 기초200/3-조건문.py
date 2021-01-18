# 1151
# n = int(input())
# print('small' if n<10 else '')

# 1152
# n = int(input())
# print('small' if n<10 else 'big')

# 1153
# a, b = map(int, input().split())
# if a>b: p='>'
# elif b>a: p='<'
# else: p='='
# print(p)

# 1154
# a, b = map(int, input().split())
# print(abs(a-b))

# 1155
# n = int(input())
# print('multiple' if n%7==0 else 'not multiple')

# 1156
# n = int(input())
# print('odd' if n%2==1 else 'even')

# 1157
# n = float(input())
# print('win' if 50<=n<=60 else 'lose', end="")

# 1158
# n = int(input())
# print('win' if 30<=n<=40 or 60<=n<=70 else 'lose', end="")

# 1159
# n = int(input())
# print('win' if 50<=n<=70 or n%6==0 else 'lose', end="")

# 1160
# n = int(input())
# print('oh my god' if n==1 or n==3 or n==5 or n==7 else 'enjoy', end="")

# 1161
# a, b = map(int, input().split())
# aa = '짝수' if a%2==0 else '홀수'
# bb = '짝수' if b%2==0 else '홀수'
# cc = '짝수' if (a+b)%2==0 else '홀수'
# print(aa+"+"+bb+"="+cc)

# 1162
# y, m, d = map(int, input().split())
# r = y - m + d
# print('대박' if str(r)[-1] == '0' else '그럭저럭')

# 1163
# y, m, d = map(int, input().split())
# r = y + m + d
# print('대박' if int(str(r)[-3])%2 == 0 else '그럭저럭')

# 1164 터널 통과하기 1
# listVal = list(map(int, input().split()))
# n=""
# for _ in listVal:
#     if _ <= 170:
#         n = "CRASH"
#         break

# if n !="CRASH": n = "PASS"
# print(n)

# 1165
# t, s = map(int, input().split())

# for time in range(90-t):
#     if time % 5 == 0: s += 1
# print(s)

# 1166 윤년 판별
# y = int(input())
# print("yes" if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else "no" )

# 1167 두 번째로 작은 수
# listVal = list(map(int, input().split()))
# listVal.sort()
# print(listVal[1])

# 1168 나이계산1
# birth, v = input().split()
# birth = int(birth[:2])
# v = int(v)
# if v == 1 or v == 2:
#     age = 100-birth+12+1
# else:
#     age = 12-birth+1
# print(age)

# 1169 나이계산2 1900년대 생이면 1 2000년대 생이면 3
# age = int(input())
# if age > 13:
#     print(112-age+1, 1)
# else:
#     print(13-age, 3)

# 1170
# g, c, i = input().split()
# if int(i)<10:
#     num = g+c+'0'+i
# else:
#     num = g+c+i
# print(num)

# 1171
# g, c, i = map(int, input().split())
# print("%d%02d%03d"%(g,c,i))

# 1172
# listVal = list(map(int, input().split()))
# listVal.sort()
# # listVal.reverse()
# for _ in listVal:
#     print(_, end=" ")

# 1173 30분 전의 시간 출력하기
# h, m = map(int, input().split())

# if m<30:
#     h -= 1
#     m -= 30
#     m = 60 + m
# else:
#     m-=30

# if h<0: h = 23

# print(h, m)

# 1180
# n = int(input())
# a = n // 10
# b = n % 10
# r = (b*10+a)*2

# if r >= 100: r = r % 100
# print(r)
# print('GOOD' if r <= 50 else 'OH MY GOD')

# 1201
# n = int(input())
# if n > 0: r = '양수'
# elif n < 0: r = '음수'
# else: r = '0'
# print(r)

# 1202
# n = int(input())

# if n >= 90: print('A')
# elif n >= 80: print('B')
# elif n >= 70: print('C')
# elif n >= 60: print('D')
# else: print('F')

# 1203
# n = int(input())
# if n <= 10: print('정상')
# elif n <= 20: print('과체중')
# else: print('비만')

# 1204 영어 서수 표현
# n = int(input())
# if n//10!=1 and n%10==1:
#     print(str(n)+"st")
# elif n//10!=1 and n%10==2:
#     print(str(n)+"nd")
# elif n//10!=1 and n%10==3:
#     print(str(n)+"rd")
# else:
#     print(str(n)+"th")

# 1205
# a, b = map(int, input().split())
# listVal = []
# listVal.append(a+b)
# listVal.append(a-b)
# listVal.append(b-a)
# listVal.append(a*b)
# listVal.append(a/b)
# listVal.append(b/a)
# listVal.append(a**b)
# listVal.append(b**a)

# listVal.sort()
# print("%.6f"%listVal[-1])

# 1206
# a, b = map(int, input().split())

# if a%b==0:
#     print("%d*%d=%d" %(b, a//b,a))
# elif b%a==0:
#     print("%d*%d=%d" %(a, b//a,b))
# else:
#     print("none")

# 1207
# listVal = list(map(int, input().split()))
# count = 0
# for _ in listVal:
#     if _ == 1: count += 1

# if count == 1: print('도')
# elif count == 2: print('개')
# elif count == 3: print('걸')
# elif count == 4: print('윷')
# else: print('모')

# 1210
# menu = {1:400, 2:340, 3:170, 4:100, 5:70}
# a, b = map(int, input().split())

# price = menu[a] + menu[b]
# print('angry' if price > 500 else 'no angry')

# 1212 삼각형 성립 조건
# length = list(map(int, input().split()))
# length.sort()
# if length[-1] < length[0] + length[1]: print('yes')
# else: print('no')

# 1214 이 달은 며칠까지 있을까?
# 2월달이면 윤달인지 한번 체크
# y, m = map(int, input().split())

# def checkmonth(m):
#     if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
#         return 31
#     else:
#         return 30

# if m == 2:
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0): print(29)
#     else: print(28)
# else:
#     print(checkmonth(m))

# 1216 컨설팅 회사
# a, b, c = map(int, input().split())

# if a == b-c: print('does not matter')
# elif a < b-c: print('advertise')
# else: print('do not advertise')

# 1218 삼각형 판단하기
# length = list(map(int, input().split()))
# length.sort()
# if length[-1] < length[0] + length[1]:
#     if length[0] == length[1] == length[2]: print('정삼각형')
#     elif length[0] == length[1] != length[2] or length[0] == length[2] != length[1] or length[2] == length[1] != length[0]: print('이등변삼각형') 
#     elif (length[0]*length[0] + length[1]*length[1]) == length[2]*length[2]: print('직각삼각형')
#     else: print('삼각형')
# else: print('삼각형아님')

# 1222 축구의 신2
# h, a, b = map(int, input().split())

# for time in range(90-h):
#     if time % 5 == 0: a += 1

# if a>b: print('win')
# elif a<b: print('lose')
# else: print('same')

# 1224 분수 크기 비교
# a, b, c, d = map(int, input().split())
# e = float(a/b)
# f = float(c/d)

# if e > f: print('>')
# elif e == f: print('=')
# else: print('<')

# 1226 이번 주 로또
# lotto = list(map(int, input().split()))
# bonus = lotto[-1]
# lotto.remove(bonus)
# user = list(map(int, input().split()))

# count = 0
# for i in lotto:
#     for j in user:
#         if i == j: count+=1

# flag = 0
# for _ in user:
#     if _ == bonus: flag = 1

# if count == 6: print(1)
# elif count == 5 and flag == 1: print(2)
# elif count == 5: print(3)
# elif count == 4: print(4)
# elif count == 3: print(5)
# else: print(0)

# 1228 비만도 측정1
# h, w = map(float, input().split())
# stand = (h - 100) * 0.9
# result = (w - stand) * 100 / stand

# if result <= 10: print('정상')
# elif result <= 20: print('과체중')
# else: print('비만')

# 1229 비만도 측정2
# h, w = map(float, input().split())

# if h < 150: stand = (h - 100)
# elif h < 160: stand = (h - 150)/2 + 50
# else: stand = (h - 100) * 0.9

# result = (w - stand) * 100 / stand

# if result <= 10: print('정상')
# elif result <= 20: print('과체중')
# else: print('비만')

# 1230 터널 통과하기 2
# listVal = list(map(int, input().split()))
# n="N"
# for _ in listVal:
#     if _ <= 170:
#         n = "CRASH "+str(_)
#         break

# if n[0] !="C": n = "PASS"
# print(n)


# 1231 계산기 1
n = input()

for _ in n:
    if _ == '+': oper = '+'
    elif _ == '-': oper = '-'
    elif _ == '*': oper = '*'
    elif _ == '/': oper = '/'
    else: continue

if oper == '/': print("%.2f" % eval(n))
else: print(eval(n))


# print(eval(n))















    


