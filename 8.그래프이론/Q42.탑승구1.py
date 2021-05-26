# 21 05 25 16:45 ~ 17:35 (50분)
'''
4
3
4
1
1

4
6
2
2
3
3
4
4
'''
################## unionSet ##################
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

G = int(input())
P = int(input())

# 자기 자신으로 초기화
parent = [0]*(G+1)
for i in range(1, G+1):
    parent[i] = i

result = 0
for i in range(P):
    data = int(input())
    root = find_parent(parent, data)
    if root == 0:
        break
    union_parent(parent, root, root-1)
    result += 1

print(result)





##########################################
# 떠오른 생각으로 풀었으나 시간초과!!
# G = int(input())
# P = int(input())
# plains = []

# for i in range(P):
#     plains.append(int(input()))

# parents = [0]*(G+1)


# for value in plains:
#     flag = False
#     for i in range(value, 0, -1):
#         if parents[i] != 1:
#             parents[i] = 1
#             flag = True
#             break
#     if flag == False: break
            

# # print(parents)
# print(parents.count(1))