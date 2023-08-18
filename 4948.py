import sys

arr = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n + 1, 2 * n + 1):
        cnt = 0
        if i == 0 or i == 1 or i == 2:
            arr.append(2)
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    cnt += 1
                    break
            if cnt == 0:
                arr.append(i)
    print(len(set(arr)))
    arr.clear()