'''
3321 최고의 피자 0123 09:25 ~ 09:55
"최고의 피자"의 1 달러 당 열량의 수를 구하라. 총칼로리/총가격
'''
from itertools import combinations

toping_num = int(input())
dow_price, toping_price = map(int, input().split())
dow_kcal = int(input())
toping_kcal = []
for i in range(toping_num):
    m = int(input())
    toping_kcal.append(m)

'''
칼로리가 높은 순서대로 측정한다.
https://1-level-up.tistory.com/7 참고함
'''
toping_kcal.sort(reverse=True)
best = dow_kcal/dow_price
price = dow_price
kcal = dow_kcal
# print(best)
for i in range(len(toping_kcal)):
    price += toping_price
    kcal += toping_kcal[i]
    if best < kcal/price:
        best = kcal/price
        # print(best, kcal)
    else: break

print(int(best))


'''
200, [50, 300, 100]
combination으로 조합 만들고, 갯수와 합을 담아두는 list를 만들자
그 후 list를 돌면서 계산 후 list sort하기 => 메모리 초과!
'''
# topingCombi = []
# Combilist = []
# for i in range(1, toping_num+1):
#     topingCombi.append(list(combinations(toping_kal, i)))

# for i in topingCombi:
#     for j in i:
#         Combilist.append([len(j), sum(j)])
# print(Combilist)

# bestcal = []
# maxVal = 0
# for x in Combilist:
#     TotalKcal = x[1] + dow_kal
#     TotalPrice = toping_price*x[0] + dow_price
#     BestKcal = TotalKcal // TotalPrice
#     # print(BestKcal)
#     # bestcal.append(BestKcal)
#     if maxVal < BestKcal: maxVal=BestKcal

# # bestcal.sort()
# # print(bestcal[-1])
# print(maxVal)