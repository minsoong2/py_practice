import sys

a, b = map(int, sys.stdin.readline().split())

re = 1
for i in range(b):
    re *= (a-i)
for i in range(b):
    re = re//(b-i)
print(re % 10007)