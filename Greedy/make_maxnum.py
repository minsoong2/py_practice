import sys

cnt_string = sys.stdin.readline().strip()
sum = 0
for i in cnt_string:
    if sum == 0 or sum == 1:
        sum += int(i)
    else:
        if int(i) == 0 or int(i) == 1:
            sum += int(i)
        else:
            sum *= int(i)
print(sum)