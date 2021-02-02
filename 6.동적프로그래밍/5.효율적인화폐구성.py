'''
5. 효율적인 화폐 구성
나누기 한 후 min값? 
a(i) = min(a(i), a(i-k)+1) (k는 coin의 단위중 하나)
3 7
2
3
5
'''
n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

a = [987654321] * 1001
a[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        if a[j-coins[i]] != 987654321:
            a[j] = min(a[j], a[j-coins[i]]+1)

# for i in range(m+1):
#     print(a[i], end=" ")

if a[m] == 987654321: print(-1)
else: print(a[m])
    
