# 2021 04 10 21:55 ~ 22:40 

def solution(s):
    answer = 0
    n = len(s)
    nList = []
    
    for step in range(1, n//2+1):
        # 압축 문자열 만들기
        zipString = ''
        count = 1
        temp = s[0:step]
        index = 0
        # print(1, n, step)
        for i in range(step, n, step):
            # if i == 0: continue
            # print(temp, s[i:i+step], i, i+step)
            
            if temp == s[i:i+step]:
                count += 1
            else:
                if count == 1:
                    zipString += temp
                else:
                    zipString += str(count) + temp
                count = 1
                
            temp = s[i:i+step]
            
        if count == 1:
            zipString += temp
        else:
            zipString += str(count) + temp
        
        # print("zipString:", zipString)
        
        index += 1
        
        # 생성된 압축 문자열 길이를 배열에 저장
        nList.append(len(zipString))
    # n//2 그 다음의 생성될 길이 추가
    nList.append(n)
    nList.sort()
    answer = nList[0]
    
    return answer