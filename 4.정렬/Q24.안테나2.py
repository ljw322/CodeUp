# 21 05 13 17:10 ~ 30(20분)

n = int(input())
nList = list(map(int, input().split()))

nList.sort()

print(nList[int(len(nList)/2-1)])