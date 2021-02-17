'''
2 위에서 아래로 15분 1초 128MB ~13:35
'''
array = []
n = int(input())
for i in range(n):
    array.append(int(input()))
array.sort(reverse = True)

for x in array:
    print(x, end=" ")
