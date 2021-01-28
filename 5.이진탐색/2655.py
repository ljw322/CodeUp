'''
2655 1차 함수의 x절편 구하기
y = ax + b (a, b입력)
-b/a
'''
a, b = map(int, input().split())

x = (-1) * b / a
print("%.4f" % x)
