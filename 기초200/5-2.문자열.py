# 1406 : love
# word = input()
# if word=="love":print("I love you.")
# else: pass

# 1408 : 암호 처리
# password = input()
# for _ in password:
#     print(chr(ord(_)+2), end="")
# print()
# for _ in password:
#     print(chr((ord(_)*7)%80+48), end="")

# 1414 : C언어를 찾아라
# word = input()
# a = 0
# b = 0
# for i in range(len(word)):
#     # print(word[i:i+2])
#     if word[i] == 'c' or word[i] == 'C': a += 1
#     if word[i:i+2] == 'cc' or word[i:i+2] == 'Cc' or word[i:i+2] == 'cC' or word[i:i+2] == 'CC': b+=1
# print(a)
# print(b)

# 1418 : t를 찾아라
# sen = input()
# for _ in range(len(sen)):
#     if sen[_]=='t': print(_+1, end=" ")

# 1419 : love 2
# sen = input()
# count = 0
# i = 0
# while i < len(sen):
#     # print(i, sen[i:i+4])
#     if sen[i:i+4] == 'love':
#         count += 1
#         i += 4
#     else: i += 1
# print(count)

# 1733 : I.O.I
# n = input()
# if n == 'IOI': print('IOI is the International Olympiad in Informatics.')
# else: print('I don\'t care.')

# 1734 : welcome!
# n = input()
# print('welcome!', n)

# 1754 : 큰 수 비교
# a, b = map(int, input().split())
# if a > b: print(b, a)
# else: print(a, b)

# 1990 : 3의 배수 판별하기
# n = int(input())
# if n%3==0: print(1)
# else: print(0)

# 2721 : 순환 문자열
s1 = input()
s2 = input()
s3 = input()
if s1[-1] == s2[0] and s2[-1] == s3[0] and s3[-1] == s1[0]: print('good')
else: print('bad')











