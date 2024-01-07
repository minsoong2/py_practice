a, b = map(int, input().split())
c = int(input())
n = int(input())

if 0<=abs(a)<=100 and 0<=abs(b)<=100:
    if 1 <= c <= 100 and 1 <= n <= 100:
        if a * n + b <= c * n and a <= c:
            print(1)
        else:
            print(0)