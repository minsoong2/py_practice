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

# while True:
#     if num % div_num == 0:
#         num = num / div_num
#         cnt += 1
#     else:
#         num = num - 1
#         cnt += 1
#
#     if num == 1:
#         break
#
# print(cnt)