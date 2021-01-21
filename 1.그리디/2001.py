'''
2001 최소대금 12:34~


'''
pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input())
juice1 = int(input())
juice2 = int(input())

pasta = [pasta1, pasta2, pasta3]
juice = [juice1, juice2]

pasta.sort()
juice.sort()

sumPrice = pasta[0] + juice[0]
result = sumPrice + sumPrice*0.1

print("%.1f"%(round(result, 1)))