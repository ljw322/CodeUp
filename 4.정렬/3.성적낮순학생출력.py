'''
3 성적이 낮은 순서로 학생 출력하기 20분 1초 128MB ~13:43
성적이 낮은 순서대로 학생 이름 출력
'''
n = int(input())

array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

result = sorted(array, key = lambda s:s[1])

for x in result:
    print(x[0], end=" ")
