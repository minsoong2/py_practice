a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
l = []
for i in range(a-2):
    sum = 0
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            sum = arr[i]+ arr[j] + arr[k]
            if sum <= b:
                l.append(sum)
print(max(l))