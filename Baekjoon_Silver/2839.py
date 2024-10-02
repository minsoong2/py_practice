value = int(input())
a = value // 5
remain = value % 5
if a >= 2:
    if remain == 0:
        print(a)
    if remain == 1 or remain == 3:
        print(a + 1)
    if remain == 2 or remain == 4:
        print(a + 2)
elif 1 <= a < 2:
    if remain == 4:
        print(a + 2)
    if remain == 2:
        print(-1)
    if remain == 1 or remain == 3:
        print(a + 1)
    if remain == 0:
        print(a)
else:
    if remain == 4:
        print(-1)
    if remain == 3:
        print(a + 1)