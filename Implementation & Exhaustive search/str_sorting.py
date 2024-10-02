import sys

input_data = sys.stdin.readline().rstrip()
str_list = list()
num_sum = 0
for c in input_data:
    if (c == '1' or c == '2' or c == '3' or c == '4' or c == '5'
            or c == '6' or c == '7' or c == '8' or c == '9' or c == '0'):
        num_sum += int(c)
    else:
        str_list.append(c)

str_list.sort()

for i in str_list:
    print(i, end='')
print(num_sum)

