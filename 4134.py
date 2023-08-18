import sys

num = int(sys.stdin.readline())
l = []
for i in range(num):
    l.append(int(sys.stdin.readline()))

for i in range(len(l)):

    while True:
        cnt = 0
        if l[i] == 0 or l[i] == 1 or l[i] == 2:
            print(2)
            break
        for k in range(2, int(l[i] ** 0.5) + 1):
            if (l[i]) % k == 0:
                cnt += 1
                break
        if cnt == 0:
            print(l[i])
            break
        l[i] += 1