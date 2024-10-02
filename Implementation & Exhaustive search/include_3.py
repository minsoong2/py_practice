import sys

hour = int(sys.stdin.readline())
cnt = 0

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
print(cnt)