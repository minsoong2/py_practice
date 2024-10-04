# array[i][j] : i행 j열에 존재하는 금의 양
# dp[i][j] : i행 j열까지의 최적의 해
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    m, n = map(int, sys.stdin.readline().split())
    input_data = list(map(int, sys.stdin.readline().split()))
    dp = []

    for j in range(m):
        dp.append(input_data[j*n: j*n + n])

    for col in range(1, n):
        for row in range(m):
            if row == 0:
                left_up = 0
            else: left_up = dp[row - 1][col - 1]
            if row == m - 1:
                left_down = 0
            else: left_down = dp[row + 1][col - 1]
            left = dp[row][col - 1]
            dp[row][col] += max(left, left_up, left_down)

    max_value = 0
    for row in range(m):
        max_value = max(max_value, dp[row][n-1])
    print(max_value)