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
    for j in prime_arr:
        check = even - j
        if j > check:
            break
        if prime_counter[check] == 1 and j <= check:
            cnt += 1
    print(cnt)