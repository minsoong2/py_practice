num = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(num):
    if arr[i] != 1:
        for j in range(2, arr[i] + 1):
            if arr[i] == j:
                cnt += 1
            if arr[i] % j == 0:
                break
            else:
                continue

print(cnt)