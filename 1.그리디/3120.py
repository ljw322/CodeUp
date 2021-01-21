'''
3301 리모컨 0121 16:35 ~ 17:00
버튼 누름의 최소 횟수는? +1 -1 +5 -5 +10 -10
https://tired-overtime.tistory.com/93 참고함
온도를 올리기만 하자.(낮추는 경우 swap)
input 7 34
output 5
'''
a, b = map(int, input().split())
if a >= b:
    temp = b
    b = a
    a = temp

count = 0
diff = b - a
while True:
    # print("diff:", diff)
    if diff > 7:
        diff -= 10
    elif diff > 3:
        diff -= 5
    elif diff >=1:
        diff -= 1
    elif diff < 0:
        diff *= -1
        continue
    elif diff == 0: break
    
    count+=1
print(count)