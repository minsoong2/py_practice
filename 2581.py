a = int(input())
b = int(input())
arr = [_ for _ in range(a, b+1)]
re = []
cnt = 0
for i in range(b - a + 1):
    if arr[i] != 1:
        for j in range(2, arr[i] + 1):
            if arr[i] == j:
                cnt += 1
                re.append(arr[i])
            if arr[i] % j == 0:
                break
            else:
                continue
if cnt == 0:
    print(-1)
else:
    print(sum(re))
    print(min(re))