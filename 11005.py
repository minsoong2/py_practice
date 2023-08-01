chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a, b = map(int, input().split())
remain = 0
l = []
while True:
    remain = a % b
    l.append(remain)
    if a < b:
        break
    a = a // b
l = l[::-1]
for i in range(len(l)):
    print(str(chars[l[i] % b]), end='')