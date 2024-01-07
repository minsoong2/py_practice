arr = list(map(int, input().split()))
re_x, re_y = 0, 0
if -999 <= arr[0] <= 999 and -999 <= arr[1] <= 999 and -999 <= arr[2] <= 999 and -999 <= arr[3] <= 999 and -999 <= arr[4] <= 999 and -999 <= arr[5] <= 999:
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if arr[0]*x + arr[1]*y == arr[2] and arr[3]*x + arr[4]*y == arr[5]:
                print(x, y)