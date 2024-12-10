import sys
from itertools import combinations

n = int(sys.stdin.readline())
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c_arr = []

for i in range(1, len(arr) + 1):
    for j in list(combinations(arr, i)):
        num_list = []
        for k in range(len(j)):
            num_list.append(j[k])
        num_list.sort(reverse=True)

        str_num = ''
        for l in num_list:
            str_num = str_num + str(l)

        c_arr.append(int(str_num))

c_arr.sort()
if n < 1023:
    print(c_arr[n])
else:
    print(-1)