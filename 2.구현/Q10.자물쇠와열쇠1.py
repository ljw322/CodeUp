# 2021 04 10 22:55 ~ 

def rotate(a):
    n = len(a)      #행
    m = len(a[0])   #열
    result = [[0] * (n) for i in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
    
def check(new_lock):
    n = len(new_lock)//3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True
    
    
def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)
    
    # 자물쇠 크기를 세배로
    new_lock = [[0] * (3*n) for i in range(3*n)]

    # 새로운 자물쇠 가운데에 자물쇠 값 대입
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠 끼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                #모두 1인지 확인
                if check(new_lock) == True: return True
                
                #열쇠 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                        
    return False