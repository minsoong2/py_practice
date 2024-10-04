import sys

num = int(sys.stdin.readline())
power_list = list(map(int, sys.stdin.readline().split()))

now = power_list[0]
cnt = 0
for i in range(1, len(power_list)):
    if now < power_list[i]:
        cnt += 1
    now = power_list[i]

print(cnt)