import sys
import math

case = int(sys.stdin.readline())

for _ in range(case):
    r, n = map(int, sys.stdin.readline().split())
    re = math.factorial(n)
    div = math.factorial(r) * math.factorial(n-r)
    print(re//div)