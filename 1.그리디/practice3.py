'''
#03 문자열 뒤집기 14:31 ~ 14:51
모두 0 또는 1로 표현하기 위한 최소 횟수 출력
input 0001100
output 1
00111
연속된 0의 개수, 연속된 1의 개수를 세면 되지 않을까 이 둘의 최소 값
'''
arr = input()
count0 = 0
count1 = 0

a = int(arr[0])
for i in range(1, len(arr)):
    if arr[i] != arr[i-1] and int(arr[i]) == 0: count1 +=1
    if arr[i] != arr[i-1] and int(arr[i]) == 1: count0 +=1

if int(arr[-1]) == 0: count0 += 1
else: count1 += 1

print(min(count0, count1))

