# a_(i-k) o -> a_i = min(a_i, a_(i-k) + 1)
# a_(i-k) x -> a_i = INF
import sys

cnt, money = map(int, sys.stdin.readline().split())
unit = [0] * cnt

for i in range(cnt):
    unit[i] = int(sys.stdin.readline())

dp_table = [10001] * (money + 1)
dp_table[0] = 0

for i in range(cnt):
    for j in range(unit[i], money + 1):
        if dp_table[j - unit[i]] != 10001:
            dp_table[j] = min(dp_table[j], dp_table[j - unit[i]] + 1)

if dp_table[money] == 10001:
    print(-1)
else:
    print(dp_table[money])