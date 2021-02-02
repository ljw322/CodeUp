'''
동적프로그래밍 - top down vs bottom up(recommendation)
                recursion vs loop
fibo
A(n) = A(n-1) + A(n-2) (n >= 3, A(1) = 1, A(2) = 1)
1 1 2 3 5 8 13 21 34 55 89
'''

a = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if a[x] != 0:
        return a[x]
    else:
        a[x] = fibo(x-1) + fibo(x-2)
        return a[x]

n = int(input())

print(fibo(n))