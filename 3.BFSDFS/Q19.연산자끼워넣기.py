# 21 05 13 13:52 ~ 14:05 (틀!!) -> DFS로 해결
'''
6
1 2 3 4 5 6
2 1 1 1
print(int(-11/2))
print(-11//2)

'''
n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minValue = 1e9
maxValue = -1e9

def dfs(i, now):
    global minValue, maxValue, n, add, sub, mul, div

    if i == n:
        minValue = min(minValue, now)
        maxValue = max(maxValue, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + nums[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - nums[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1, now * nums[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now / nums[i]))
            div += 1


dfs(1, nums[0])

print(maxValue)
print(minValue)


