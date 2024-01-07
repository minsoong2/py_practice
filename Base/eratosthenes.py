def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

n = 100
prime_numbers = sieve_of_eratosthenes(n)
print(prime_numbers)
