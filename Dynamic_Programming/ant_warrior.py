# a_i = max(a_(i-1), a_(i-2) + k_i)
import sys

num = int(sys.stdin.readline())
cnt_list = list(map(int, sys.stdin.readline().split()))

dp_table = [0] * 100

dp_table[0] = cnt_list[0]
dp_table[1] = max(cnt_list[0], cnt_list[1])
for i in range(2, len(cnt_list)):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + cnt_list[i])

print(dp_table[len(cnt_list) - 1])