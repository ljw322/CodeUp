# 1이 될 때까지
# 나누어 떨어지는 지 확인.
n, m = map(int, input().split())

count = 0
while n >= 1:
    if n == 1: break

    if n % m == 0:
        n = int(n // m)
        count += 1
    else:
        if n < m :
            count += n-1
            n = 1
        else:
            k = n // m * m
            count += n - k
            n = k
    
    print(n)

print(count)