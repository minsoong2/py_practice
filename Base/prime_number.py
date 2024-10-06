import sympy
import math

n = 100
prime_numbers = list(sympy.primerange(0, n))
print(prime_numbers)  # 0부터 n까지의 소수 목록 출력

def is_prime_number(num):
    for i in range(2, num):
        if num % i != 0:
            return True
    return False

def is_prime_number_2(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i != 0:
            return True
    return False

print(is_prime_number_2(7))