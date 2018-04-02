import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prime_generator(n):
    for i in range(n):
        if is_prime(i):
            yield i


def get_factors(n):
    factors = []
    for i in prime_generator(n):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if factors == []:
        factors = [1, n]
    return factors


def sum_lowest_factors(n):
    max_f = max(get_factors(n))
    return max_f + int(n / max_f)


print(sum_lowest_factors(12))
print(sum_lowest_factors(456))
print(sum_lowest_factors(4567))
print(sum_lowest_factors(12345))
print(sum_lowest_factors(345678))
