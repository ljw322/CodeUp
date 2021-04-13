'''
21 04 10 17:50 ~ 17:57
K1KA5CB7
AJKDLSI412K4JSJ9D
'''

string = input()
numList = []
alpList = []
answer = ''

for value in string:
    if ord(value) >= ord('0') and ord(value) <= ord('9'):
        numList.append(int(value))
    else:
        alpList.append(value)


alpList.sort()
# print(alpList)

for value in alpList:
    answer += value

answer += str(sum(numList))
print(answer)



