# import sys
# a, b = map(int, sys.stdin.readline().split())
# c, d = map(int, sys.stdin.readline().split())
# numerator = a * d + c * b
# denominator = b * d
# m = max(numerator, denominator)
# for i in range(m, 0, -1):
#     if numerator % i == 0 and denominator % i == 0:
#         numerator = numerator // i
#         denominator = denominator // i
#         print(numerator, denominator)
#         break
### 시간초과 ###

import sys


def gcd(n, d):
    while d:
        n, d = d, n % d
    return n


a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
numerator = a * d + c * b
denominator = b * d

gcd = gcd(numerator, denominator)

print(numerator // gcd, denominator // gcd)