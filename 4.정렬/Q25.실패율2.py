# 2021 05 13 17:25 ~ 46 . divided by 0 예외상황 생각해줘야 함
# 계수정렬
def solution(N, stages):
    answer = []
    info = [0]*(N+2)
    realInfo = []
    
    for v in stages:
        info[v] += 1
    
    for i in range(1, N+1):
        s = 0
        for j in range(i, N+2):
            s += info[j]
        if s == 0:
            realInfo.append([i, 0])
        else:   
            realInfo.append([i, info[i]/s])
    
    print(realInfo)
    
    realInfo.sort(key=lambda x:(-x[1], x[0]))
    # print(realInfo)
    
    for v in realInfo:
        answer.append(v[0])
    
    return answer