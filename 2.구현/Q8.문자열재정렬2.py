# 21 06 08 22:30~ 22:34
'''
요약: 알파벳대문자, 숫자(0~9)를 알파벳 오름차순+숫자들의 합 출력
해결: ord()를 이용
K1KA5CB7
AJKDLSI412K4JSJ9D
'''

string = input()

result = ''
alpha = []
num = 0

print(ord('0'), ord('9'))
for value in string:
    if 48 <= ord(value) <= 57:
        num += int(value)
    else:
        alpha.append(value)

alpha.sort()

for value in alpha:
    result += value

result += str(num)

print(result)
