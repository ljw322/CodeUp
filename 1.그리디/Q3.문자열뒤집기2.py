# 21 06 07 16:15 ~ 16:29
'''
요약: 연속된 하나 이상의 숫자를 잡고 뒤집는다. 0->1 or 1->0 뒤집기 최소 횟수는?
해결: 0뭉터기, 1뭉터기 수 중 최소값
0001100
'''
s = input()

a = 0   #0에 대한 덩어리 수
b = 0   #1에 대한 덩어리 수

value = s[0]
if value == '0': a += 1
else: b += 1

for i in range(1, len(s)):
    if value != s[i] and s[i] == '0':
        a += 1
    if value != s[i] and s[i] == '1':
        b += 1
    value = s[i]

# print(a, b)
print(min(a, b))