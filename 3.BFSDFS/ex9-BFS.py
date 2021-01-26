from collections import deque
# BFS
def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True

    # 큐가 끝날 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=" ")

        # 해당 원소와 연결된, 방문하지 않은 노드 방문
        for x in graph[v]:
            if not visit[x]:
                queue.append(x)
                visit[x] = True



# graph 정보담기
graph = [
    [],
    [2,3,8],
    [1,7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7], 
]

# 방문 visit 리스트
visit =  [False] * 9

# 함수 실행
bfs(graph, 1, visit)