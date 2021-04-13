# 5658 [모의SW역량테스트] 보물상자 비밀번호
# 210402 19:45 ~ 20:45


import sys

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample_input.txt")

sys.stdin = open(file_path, "r")

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    string = input()

    turn = n // 4
    numSet = set()

    for l in range(turn):
        #string 을 4개씩 끊어서 출력시키기
        index = 0
        for j in range(4):
            pwd = ""
            for i in range(turn):
                pwd += string[index]
                index += 1
            # print(pwd, end=" ")
            numSet.add(int(pwd, 16))

        # print()
        # string의 맨앞을 삭제 후 뒤에 붙여준다. 
        temp = string[0]
        string = string[1:]
        string += temp


    # print(numSet)
    numList = list(numSet)
    numList.sort(reverse = True)
    print("#"+str(test_case), numList[k-1])
    # result = str(hex(numList[k-1]))[2:].upper()
    # print(result)
    # print(hex(numList[k-1]))



    # print(n, k, string)
