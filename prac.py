# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())

# a, b = map(int, input().split())
# arr = list(map(int, input().split())) * list 공백기준 선언 *
# list -> int는 append x
# print(i, end=' ') end='' 줄바꿈 제거
# set(list) * set -> list 중복제거 *

# l = [i for i in range(10)] * 파이썬 리스트 정의 *

# 정수 문자열 출력
# data = list(map(str, input().split()))
# num = int(data[0])
# string = data[1]

# k_v = {}
# for i in range(n):
#     k, v = map(int, input().split())
#     k_v[k] = v

# from collections import Counter
# 출력: Counter({6: 1, 3: 1, 2: 1, 10: 1, -10: 1})

# for element, count in my_counter.items():
#     print(f"{element}: {count}")

import sys
a, b = map(int, sys.stdin.readline().split())
sum = 1
m = max(a, b)
for j in range(m, 0, -1):
    if a % j == 0 and b % j == 0:
        a = a // j
        b = b // j
        sum = j * a * b
        print(sum)
        break
