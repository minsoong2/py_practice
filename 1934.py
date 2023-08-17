import sys
n = int(sys.stdin.readline())
sum = 1
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    m = max(a, b)
    for j in range(m, 0, -1):
        if a % j == 0 and b % j == 0:
            a = a // j
            b = b // j
            sum = j * a * b
            print(sum)
            break