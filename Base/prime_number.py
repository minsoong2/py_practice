import sympy

n = 100
prime_numbers = list(sympy.primerange(0, n))
print(prime_numbers)  # 0부터 n까지의 소수 목록 출력

def is_prime_number(num):
    for i in range(2, num):
        if num % i != 0:
            return True
    return False

