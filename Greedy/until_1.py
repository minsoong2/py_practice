import sys

num, div_num = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    target = (num//div_num) * div_num
    cnt += num - target
    num = target

    if num < div_num:
        break

    cnt += 1
    num //= div_num

cnt += num - 1
print(cnt)


# num, div = map(int, sys.stdin.readline().split())
# cnt = 0
#
# while True:
#     if num == 1:
#         break
#
#     if num % div == 0:
#         num = num // div
#     else:
#         num = num - 1
#     cnt += 1
#
# print(cnt)