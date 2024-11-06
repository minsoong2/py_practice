import sys

n, money = map(int, sys.stdin.readline().split())
coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))
coin_list.sort()

dp = [10001] * (money + 1)
dp[0] = 0
for coin in coin_list:
    for i in range(coin, money + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[money] == 10001:
    print(-1)
else:
    print(dp[money])
print(dp)