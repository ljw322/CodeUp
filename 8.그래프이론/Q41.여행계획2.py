'''
요약: N개의 도시. M개의 여행계획 도시
    N*N은 두 여행지가 연결되어있는지에 대한 정보
    마지막 줄 여행갈 순서 리스트 여행계획이 가능한지 ?
해결: find_parent, union_parent로 
'''

def find_parent(parent, x):
    if parent[x] != x:
        x = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = "YES"
for i in range(M-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = "NO"
print(result)
