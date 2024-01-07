a = int(input())
re = 0
for i in range(1, a+1):
    num = i + sum(map(int, str(i)))
    if a == num:
        re = i
        break
print(re)