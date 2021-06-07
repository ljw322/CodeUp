# 21 05 26 13:35 ~ 13:58 (23분) 틀림!
# https://www.acmicpc.net/problem/2887
'''
스패닝트리. 크루스칼 => 메모리(시간초과!)
=> x, y, z 각각에 대하여 최단 거리를 계산하여 road(edge)에 넣은 후, 정렬한다!
=> 기존 O(N^2)에서 O(3N)으로 시간 및 메모리가 줄어든다
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''
import sys
input = sys.stdin.readline

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

n = int(input())

parent = [0] *(n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append([data[0],i])
    y.append([data[1],i])
    z.append([data[2],i])

x.sort()
y.sort()
z.sort()

road = []
for i in range(n-1):
    road.append((x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
    road.append((y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
    road.append((z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))

# print(city)
road.sort()
# print(road)

result = 0
for value in road:
    cost, a, b = value
    if find_parent(parent, a) != find_parent(parent, b):
        # print(a, b, cost)
        union_parent(parent, a, b)
        result += cost

print(result)