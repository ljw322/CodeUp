'''
21 04 15 15:00 ~ 15:25
크루스칼로 일단 ㄱ..
v, e, edge, parent, result
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
edges = []
parent = [0]*(v+1)
result = []

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for value in edges:
    cost, a, b = value
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(value)

answer = 0
# for value in result:
#     print(value, end=" ")
for i in range(len(result)):
    if i == len(result)-1:
        continue
    answer += result[i][0]

print(answer)