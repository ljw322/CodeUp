'''
동적프로그래밍 - top down vs bottom up(recommendation)
                recursion vs loop
fibo
A(n) = A(n-1) + A(n-2) (n >= 3, A(1) = 1, A(2) = 1)
'''

a = [0]*100

a[1] = 1
a[2] = 1

n = int(input())

for i in range(3, n+1):
    a[i] = a[i-1] + a[i-2]

print(a[n])