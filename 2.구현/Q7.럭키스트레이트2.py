# 21 06 08 22:13 ~ 22:28
'''
요약: 짝수자릴수 숫자 주어질때, 왼절반 오절반 합 같으면 "LUCKY"출력, 아니면 "READY"출력
해결: len이용해서 배열접근
123402
7755
'''

number = str(input())
n = len(number)//2
left = 0
right = 0

for i in range(n):
    # print(i, n+i)
    left += int(number[i])
    right += int(number[n+i])

# print(left, right)

if left == right:
    print("LUCKY")
else:
    print("READY")
