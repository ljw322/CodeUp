# 21 05 12 16:00 ~ 20...(문제이해하는데만...^^)
# ㅠㅠㅠㅠㅠ 오래걸림..1시간. checkRight stack pop할 때 런타임에러.

def checkRight(v):
    stack = []
    
    for value in v:
        if value == '(': stack.append(value)
        else:
            if len(stack) == 0: return False
            else: stack.pop()
    
    return True
    

def dfs(p):
    #1step
    if p == '': return ''
    
    #2step - separate u,v
    acount = 0
    bcount = 0
    i = 0
    for value in p:
        if value == '(': acount += 1
        else: bcount += 1
        
        i += 1
        if acount == bcount:
            u = p[:i]
            v = p[i:]
            print(u + ", " + v)
            break
            
    #3step - check if right
    if checkRight(u) == True:
        u = u + dfs(v)
        # print('u:',u)
        return u
    else: 
        temp = '(' + dfs(v)
        temp = temp + ')'
        u = u[1:-1]
        for _ in u:
            if _ == '(': temp = temp + ')'
            else: temp = temp + '('
        
        
        # print('v:', temp)
        return temp


def solution(p):
    answer = ''
    answer = dfs(p)      
    
    return answer