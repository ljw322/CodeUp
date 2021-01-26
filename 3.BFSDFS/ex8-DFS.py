# DFS
def dfs(graph, v, visit):
    # 현재노드 방문 처리
    visit[v] = True 
    print(v, end=" ")

    # 현재 노드와 연결된 노드들을 순차적으로 방문
    for x in graph[v]:
        if not visit[x]:    # 방문하지 않았다면 ! 
            dfs(graph, x, visit)


# 주어진 정보 연결리스트에 저장 (노드 0부터 n+1까지)
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

# 노드별 방문 정보 리스트
visit = [False] * 9

# DFS 함수 호출 (노드정보, 시작점, 방문)
dfs(graph, 1, visit)