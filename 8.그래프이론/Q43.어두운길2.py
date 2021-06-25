'''
요약: 두 마을 간 가로등(가중치) 불빛 최소화. 절약할 수 있는 최대금액?
    입력 -> 집의 수 N, 도로의 수 M, (X, Y, Z)
해결: 스패닝트리
'''
from collections import deque

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] *(N+1)

for i in range(1, N+1):
    parent[i] = i

q = []

for i in range(M):
    x, y, z = map(int, input().split())
    q.append((z, x, y))

q.sort()
result = 0

for value in q:
    c, a, b = value
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        result += c

print(result)