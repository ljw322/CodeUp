# 2021 06 10 15:15~ 16:05 틀!!
'''
요약: N*N Lock에 M*M Key배열. Key는 회전과 이동 가능. 열쇠로 자물쇠 열 수 있으면 True 없으면 False
해결: 1. Lock의 3배인 newLock생성. 정가운데 Lock정보 update
    2. 4가지 방향으로 rotate하면서 => rotate(), newKey[j][m-i-1] = key[i][j]
    3. Lock의 2배만큼 순회하면서 자물쇠 끼우기
    4. 홈이 모두 일치하는지 확인 => check(), range(n, n*2):
    5. 자물쇠 빼기

'''


def rotate(key):
    m = len(key)
    rotatedKey = [[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            rotatedKey[j][m-i-1] = key[i][j]   
    
    return rotatedKey
    
def check(newLock):
    n = len(newLock)//3    
    for i in range(n, n*2):
        for j in range(n, n*2):
            if newLock[i][j] != 1:
                return False
    
    return True


def solution(key, lock):
    answer = False
    
    n = len(lock)
    m = len(key)
    newLock = [[0]*(3*n) for i in range(3*n)]
    
    # 3배로 늘린 newLock에 기존 lock 정보 대입
    for i in range(n):
        for j in range(n):
            newLock[i+n][j+n] = lock[i][j]

    # 4가지 방향으로 rotate하면서
    for rotation in range(4):
        key = rotate(key)
        # 3배로 늘린 newLock의 2배만큼 끼워보기(마지막 세칸은 끼울 필요 없)
        for i in range(n*2):
            for j in range(n*2):
                # 자물쇠 끼우기
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] += key[x][y]
                        
                if check(newLock) == True: return True
                
                # 열쇠 빼기
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] -= key[x][y]
    
    return answer