arr = list(map(int, input().split()))
arr.sort()
if arr[0] + arr[1] <= arr[2]:
    print((arr[0]+arr[1])*2 - 1)
else:
    print(arr[0]+arr[1]+arr[2])
