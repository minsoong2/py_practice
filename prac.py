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
from collections import Counter
num = int(sys.stdin.readline())

prime_arr = []
l_tf = [1] * 1000001
for i in range(2, 1000000 + 1):
    if l_tf[i]:
        prime_arr.append(i)
        for remove in range(i * 2, 1000000 + 1, i):
            l_tf[remove] = 0

for i in range(num):
    cnt = 0
    even = int(sys.stdin.readline())
    prime_counter = Counter(prime_arr)
    print(prime_counter)
    for j in prime_arr:
        check = even - j
        if j > check:
            break
        if prime_counter[check] == 1 and j <= check:
            cnt += 1
    print(cnt)