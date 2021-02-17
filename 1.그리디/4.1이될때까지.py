'''
1이 될 때까지 2021-01-19 20:45 ~ 20:57 땡 !! 틀림!! 테스트케이스 생각좀!!
25 5 => 5, 1
17 4 => 16, 4, 1
25 3 => 24, 8, 7, 6, 2, 1
'''
n, k = map(int, input().split())
count = 0

while n >= 1 :
    if n % k != 0:
        diff = n - int(n//k)*k
        count += diff
        n -=  diff

    else:
        n = int(n/k)
        count +=1
    
    print(n, end=" ")

print(count-1)

