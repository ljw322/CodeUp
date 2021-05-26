# 21 05 25 15:25 ~ 16:44 (20분) => 플로이드로 풀었음
# 본문. => 서로 연결된 노드를 같은 집합에 포함 시켜 union합집합 연산이용
# => 여행계획 도시들이 모두 같은 집합에 있는지 확인한다.
'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
########################################################
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

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = "YES"
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = "NO"

print(result)
















########################################################
# INF = int(1e9)

# n, m = map(int, input().split())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# plan = list(map(int, input().split()))

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 0: graph[i][j] = INF
#         if i == j: graph[i][j] = 0

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# # for value in graph:
# #     print(value)

# result = 'YES'
# for i in range(len(plan)-1):
#     if graph[plan[i]][plan[i+1]] == 0 or graph[plan[i]][plan[i+1]] == INF:
#         result = 'NO'
#         break
# print(result)


