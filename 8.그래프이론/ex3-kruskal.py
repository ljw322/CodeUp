'''
2021 04 14
크루스칼 알고리즘 p.290
1. 간선 오름차순 정렬
2. 간선 작은 순서대로 넣으면서 싸이클 생기는지 확인해가면서
위 1,2를 반복      
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
# v, e, parent, edges

#부모노드 찾기 == 싸이클 확인 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#같은 부모로 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)
edges = []

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
for value in edges:
    cost, a, b = value
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

    