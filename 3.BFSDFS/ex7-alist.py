'''
인접리스트로 표현하기 => 행이 n(노드 개수)인 인접리스트로 표현
       (0) 
      7   5 
    (1)    (2)
'''
graph = [[] for i in range(3)]

# (노드번호, 가중치) 로 저장
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)

