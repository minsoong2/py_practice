a, b = map(int, input().split())

# a = int(input())
# b = int(input())

if 0 <= a <= 23 and 0 <= b <= 59:
    if a > 0 and b - 45 >= 0:
        print(a, b - 45)
    elif a > 0 > b - 45:
        print(a - 1, 60 + (b - 45))
    elif a == 0 and b - 45 < 0:
        print(24 + (a - 1), 60 + (b - 45))
    elif a == 0 and b - 45 >= 0:
        print(a, b - 45)
