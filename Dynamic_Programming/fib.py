import time
# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     return fib(num - 1) + fib(num - 2)
#
# print(fib(10)) # 100 x

# Top-down fib
# d = [0] * 1000
# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#
#     # Memorization
#     if d[num] != 0:
#         return d[num]
#
#     d[num] = fib(num - 1) + fib(num - 2)
#     return d[num]
# print(fib(999))

# Bottom-up fib
# d = [0] * 100
# d[1], d[2] = 1, 1
# n = 99
#
# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]
#
# print(d[n])