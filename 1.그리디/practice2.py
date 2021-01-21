'''
#02 곱하기 혹은 더하기 14:10 ~ 14:26
문자열숫자 사이에 곱 또는 더하기를 넣어 만들 수 있응 가장 큰 수?
(연산은 왼쪽부터 진행된다)
input 02984
output 567
1111 4
0이나 1 있으면 +
그외 숫자 * 
'''
# arr = input()
# a = int(arr[0])
# for i in range(1, len(arr)):
#     plus = a + int(arr[i])
#     mul = a * int(arr[i])

#     if plus >= mul: a = plus
#     else: a = mul

# print(a)

arr = input()
a = int(arr[0])
for i in range(1, len(arr)):
    if int(arr[i]) <= 1 or a <= 1:
        a += int(arr[i])
    else:
        a *= int(arr[i])

print(a)


