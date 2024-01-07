dictionary = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
cnt = 0.0
sum = 0.0
for i in range(20):
    arr = list(map(str, input().split()))
    if arr[2] != 'P':
        cnt += float(arr[1])
        sum += float(arr[1])*dictionary.get(arr[2])
    else:
        pass

print(format(sum/cnt, '.6f'))