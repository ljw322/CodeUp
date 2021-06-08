# 21 06 07 15:45 ~ 15:52
'''
요약: 왼쪽부터 차례로 연산. + or *이용해 최대값 출력
해결: 0,1이면 더하고 그외는 다 곱해버린다.
02984
'''
s = input()
left = int(s[0])

for i in range(1, len(s)):
    right = int(s[i])
    if left <= 1 or right <= 1:
        left += right
    else:
        left *= right

print(left)