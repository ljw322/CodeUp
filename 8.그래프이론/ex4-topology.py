'''
2021 04 14
토폴로지(위상정렬) 알고리즘 p.297
1. 진입차수 0인거 큐에 삽입
2. 큐에서 빼면서 차수 빼고 인접 노드 조사
위 1,2를 반복      
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
graph []임. [0]이 아니라.
q삭제 시 pop이 아니라 popleft
'''
# v, e, indegree, graph, result
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
result = []
graph = [[] for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for value in result:
        print(value, end=" ")

topology_sort()
