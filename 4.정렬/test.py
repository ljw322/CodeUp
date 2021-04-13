
# 2. 위에서 아래로
# 3. 성적이 낮은 순서로 학생 출력하기
# 4. 두 배열의 원소 교체
'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))