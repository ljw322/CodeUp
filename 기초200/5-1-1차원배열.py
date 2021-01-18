# 1402 : 거꾸로 출력하기 3
# n = int(input())
# listVal = list(input().split())
# listVal.reverse()
# for _ in listVal:
#     print(_, end=" ")

# 1403 : 배열 두번 출력하기
# k = int(input())
# listVal = list(input().split())
# for i in range(2):
#     for _ in listVal:
#         print(_)

# 1405 : 숫자 로테이션
# k = int(input())
# listVal = list(input().split())
# for i in range(len(listVal)):
#     for _ in listVal:
#         print(_, end=" ")
#     temp = listVal[0]
#     listVal.remove(listVal[0])
#     listVal.append(temp)
#     print()

# 1407 : 문자열 출력하기 1
# sen = list(input().split())
# for _ in sen:
#     print(_, end="")

# 1409 : 기억력 테스트 1
# listVal = list(input().split())
# n = int(input())
# print(listVal[n-1])

# 1410 : 올바른 괄호 1 (괄호 개수 세기)
# sen = input()
# a = 0
# b = 0
# for i in sen:
#     if i=='(': a+=1
#     else: b+=1
# print(a, b)

# 1411 : 빠진 카드
# n = int(input())
# listVal = [0]*n
# # print(listVal)
# for i in range(n-1):
#     k = int(input())
#     listVal[k-1] = 1

# for _ in listVal:
#     if _ == 0: print(listVal.index(_)+1)

# 1412 : 알파벳 개수 출력하기
# 알파벳 소문자 a는 아스키코드로 97이다. 그리고 알파벳 개수는 26..
# sen = input()
# countList = [0]*26
# for _ in sen:
#     if 97<=ord(_)<=122:
#         countList[ord(_)-97] +=1
# i = 97
# for _ in countList:
#     print(chr(i)+":"+str(_))
#     i+=1

# 1416 : 2진수 변환
# n = int(input())
# b = bin(n)
# print(str(b)[2:])

# 1420 : 3등 찾기
# n = int(input())
# score = {}
# scoreList = []
# for i in range(n):
#     a, b = input().split()
#     score[int(b)] = a
#     scoreList.append(int(b))
# scoreList.sort()
# print(score[scoreList[-3]])

# 1425 : 자리 배치
# n, c = map(int, input().split())
# students = list(map(int, input().split()))
# students.sort()
# line = 0

# if n % c==0: line = n // c
# else: line = n // c + 1

# index = 1
# for i in students:
#     print(students[index-1], end=" ")
#     if index % c == 0: print()
#     index +=1

# 1430 : 기억력 테스트 2 -> 이진탐색.. 메모리 초과..해결못함
def binarySearch(arr, target, left, right):
    if left > right: return 0
    middle_point = (left+right)//2
    middle = arr[middle_point]
    # print(middle_point,middle)
    if target == middle: return 1
    elif target > middle: return binarySearch(arr, target, middle_point+1, right)
    elif target < middle: return binarySearch(arr, target, left, middle_point-1)
    


n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nList.sort()

for _ in mList:
    print(binarySearch(nList, _, 0, len(nList)-1), end=" ")



# 1440 : 비교
# n = int(input())
# nList = list(map(int, input().split()))
# for i in range(n):
#     value = int(nList[i])
#     print("%d: " % (i+1), end="")
#     for j in range(n):
#         if i == j: continue
#         if value > int(nList[j]): print(">", end=" ")
#         elif value < int(nList[j]): print("<", end=" ")
#         elif value == int(nList[j]): print("=", end=" ")
#     print()









