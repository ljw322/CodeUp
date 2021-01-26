# factorial

# iterative function
def factorial_loop(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result


def factorial_recur(n):
    if n <= 1: return 1
    return n * factorial_recur(n-1)


# recursive function

print('반복적 구현:', factorial_loop(5))
print('반복적 구현:', factorial_recur(5))