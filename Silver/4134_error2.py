import sys

num = int(sys.stdin.readline())
l = []
prime_number_list = []
for i in range(num):
    l.append(int(sys.stdin.readline()))
for i in range(len(l)):
    if i + 1 == len(l):
        break
    for j in range(1, l[i+1] - l[i]):
        for k in range(2, l[i] + j):
            if (l[i] + j) % k == 0:
                break
            else:
                if k == l[i] + j - 1:
                    prime_number_list.append(l[i] + j)
    print(min(prime_number_list))
    prime_number_list.clear()
while l[-1]:
    l[-1] += 1
    for k in range(2, l[-1]):
        if (l[-1]) % k == 0:
            break
        else:
            if k == l[-1] - 1:
                prime_number_list.append(l[-1])
    if len(prime_number_list) == 1:
        print(prime_number_list[0])
        break