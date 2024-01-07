a, b = map(int, input().split())

c = int(input())
# b = int(input())

if 0 <= a <= 23 and 0 <= b <= 59:
    if b + c >= 60:
        x = int((b+c) / 60)
        y = (b+c) % 60
        if a + x >= 24:
            print(a+x - 24, y)
        else:
            print(a+x, y)
    else:
        print(a, b+c)