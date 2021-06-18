# 2021 06 10 13:56 ~ 14:51 틀!! -> 이전에 푼 것 참조함.
'''
요약: 1개 이상의 단어로 문자를 잘라 문자열 압축했을 때, 최소 압축길이는?
해결: 1. len(s)//2로 쪼갠다.
    2. 문자열이 잘 쪼개졌는디 출력하면서 확인
    3. 맨 끝부분 잘 붙였는지 확인
    4. len(s)//2의 뒷부분의 문자열 길이 append

    5. 리스트에 문자열 길이를 담고, 정렬

'''

def solution(s):
    answer = 0
    List = []
    
    print(len(s)//2)
    for i in range(1, len(s)//2+1):
        result = ''
        temp = ''
        count = 1
        for j in range(len(s)//i+1):
            
            start = s[j*i:j*i+i]            
            if temp == start: count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                count = 1
            
            temp = start

        # 마지막부분 더해주기!!
        if count == 1:
            result += temp
        else:
            result += str(count) + temp
            
        # print(result)
        List.append(len(result))
        
    # n//2 다음에 생성될 길이 추가!!
    List.append(len(s))
    List.sort()
    answer = List[0]
        
    return answer