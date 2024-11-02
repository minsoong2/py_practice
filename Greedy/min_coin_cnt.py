import sys
from collections import deque

money = int(sys.stdin.readline())
coin_list = list(map(int, sys.stdin.readline().split()))
coin_list.sort(reverse=True)
coin_q = deque(coin_list)
cnt_list = []

while True:
    m = money
    cnt = 0
    for coin in coin_q:
        cnt += m // coin
        m = m % coin
    cnt_list.append(cnt)
    coin_q.popleft()

    if not coin_q:
        break

print(min(cnt_list))