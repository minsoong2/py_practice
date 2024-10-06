k = 8

for i in range(k + 1):
    print(i, '의 마지막 비트:', (i & -i))