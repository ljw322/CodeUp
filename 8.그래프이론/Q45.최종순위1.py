# 21 05 26 14:25 ~ 15:25 (60분) 틀!!!! 
'''
"낮은 등수를 가리키도록"
싸이클이 있는지도 확인해야되고, 출력순서가 여러개인지도 확인해야 한다.
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
'''
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

while T > 0:

    n = int(input())
    indegree = [0] *(n+1)
    graph = [[False] * (n+1) for i in range(n+1)]

    lastYear = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[lastYear[i]][lastYear[j]] = True
            indegree[lastYear[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1
    
    # 위상정렬 시작!!!
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    case = True     #위상정렬 결과가 오직 한가지 인지 확인
    cycle = False    #싸이클이 존재하는지 확인

    for i in range(n):   #노드 개수 만큼 반복
        
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            case = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1

                #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)


    if cycle:
        print("IMPOSSIBLE")
    elif not case:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print() # 다음 케이스를 위해 개행문 출력


    T -= 1

