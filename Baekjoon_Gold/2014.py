import sys
import heapq

k, n = map(int, sys.stdin.readline().split())
prime_list = list(map(int, sys.stdin.readline().split()))
q = []

for prime in prime_list:
    heapq.heappush(q, prime)

re = []
while q:
    num = heapq.heappop(q)
    re.append(num)
    for prime in prime_list:
        heapq.heappush(q, num * prime)

        if num % prime == 0:
            break

    if len(re) == n:
        break

print(re[n-1])