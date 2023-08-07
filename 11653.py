a = int(input())
num = 0
for i in range(a - 1, 0, -1):
    if a % i == 0:
        num = a // i
        print(num)
        a = a // num