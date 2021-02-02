'''
연산의 최소값은?
1. 5로 나누어지는지
2. 3으로 나누어지는지
3. 2로 나누어지는지
4. 1 빼기

=> bottom up 방식으로 해보자
'''

x = int(input())
a = [0] * 30001      # 참고로 a[1] = 0이다.

for i in range(2, x+1):
    a[i] = a[i-1] + 1
    temp = a[i]

    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
    
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1)

    if i % 5 == 0:
        a[i] = min(a[i], a[i//5] + 1)
    print(i, temp, a[i])

for x in range(0, x+1):
    print(a[x], end=" ")




