result_dict = {}
for i in range(10):
    result_dict[i] = 0

num = int(input())
p = 1
for j in range(len(str(num))):
    s = int(str(num//10) + "9")
    for i in range(10):
        result_dict[i] += (num//10+1) * p
    for i in range(10-(s-num), 10):
        result_dict[i] -= p
    for i in list(str(num)[:-1]):
        i = int(i)
        result_dict[i] -= (s-num) * p
    result_dict[0] -= p
    num //= 10
    p *= 10


for l in result_dict.values():
    print(l, end=' ')