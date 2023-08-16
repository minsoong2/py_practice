import sys

a, b = map(int, sys.stdin.readline().split())
l_1 = set(list(map(int, sys.stdin.readline().split())))
l_2 = set(list(map(int, sys.stdin.readline().split())))

re_1 = l_1 - l_2
re_2 = l_2 - l_1
print(len(re_1)+len(re_2))