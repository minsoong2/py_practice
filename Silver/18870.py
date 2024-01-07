import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
copy_l = list(set(l))
copy_l.sort()
index_dict = {value: index for index, value in enumerate(copy_l)}

for num in l:
    print(index_dict[num], end=' ')