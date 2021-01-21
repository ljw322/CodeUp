'''
3301 거스름돈 0121 12:30 ~ 12:33
거스름돈을 입력받는다.
50000원, 10000원, 5000원, 1000원, 500원, 100원, 50원, 10원
input 54520
output 8
'''
coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

money = int(input())

count = 0
for _ in coin:
    count += int(money // _)
    money = int(money % _)

print(count)


