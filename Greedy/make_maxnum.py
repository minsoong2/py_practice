import sys

num_str = sys.stdin.readline().strip()
num_list = []
for idx in range(len(num_str)):
    num_list.append(int(num_str[idx]))

num_max = 0
for num in num_list:
    if num_max == 0 or num_max == 1:
        num_max += num
    else:
        num_max *= num

print(num_max)