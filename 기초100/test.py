from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']
p_result = list(permutations(data, 3))
c_result = list(combinations(data, 3))
product_result = list(product(data, repeat=3))
crp_result = list(combinations_with_replacement(data, 3))

print(len(p_result) , "\n" , p_result)
print(len(c_result) , "\n" , c_result)
print(len(product_result) , "\n" , product_result)
print(len(crp_result) , "\n" , crp_result)