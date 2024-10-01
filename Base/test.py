import sys

num, div_num = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    if num % div_num == 0:
        num = num / div_num
        cnt += 1
    else:
        num = num - 1
        cnt += 1

    if num == 1:
        break

print(cnt)