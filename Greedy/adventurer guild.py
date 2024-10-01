import sys
from tokenize import group

cnt = int(sys.stdin.readline())
fear_list = list(map(int, sys.stdin.readline().split()))
fear_list.sort()

group_num = 0
group_cnt = 0

for i in range(cnt):
    group_num += 1
    if group_num >= fear_list[i]:
        group_num = 0
        group_cnt += 1

print(group_cnt)
