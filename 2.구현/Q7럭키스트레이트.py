'''
21 04 10 17:45 ~ 17:48
정답
'''

number = input()
n = len(number)//2

a = 0
b = 0

for i in range(0, n):
    a += int(number[i])

for j in range(n, len(number)):
    b += int(number[j])

# print(a, b)
if a == b: print("LUCKY")
else: print("READY")
