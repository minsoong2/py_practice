import sys
from collections import Counter
num = int(sys.stdin.readline())

prime_arr = []
l = []
for _ in range(num):
    even = int(sys.stdin.readline())
    l.append(even)
M = max(l)

if M > 2 and M % 2 == 0:
    for i in range(2, M + 1):
        cnt = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            prime_arr.append(i)
    prime_arr = list(set(prime_arr))

for i in range(len(l)):
    cnt = 0
    even = l[i]
    prime_counter = Counter(prime_arr)
    for j in prime_arr:
        check = even - j
        if j > check:
            break
        if prime_counter[check] == 1 and j <= check:
            cnt += 1
    print(cnt)