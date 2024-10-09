# 가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence, LIS)
# dp
# d[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i, d[i] = max(d[i], d[j] + 1) if arr[j] <= arr[i]

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.reverse()
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if n_list[i] >= n_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp[n-1])