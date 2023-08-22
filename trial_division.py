prime_arr = []
for i in range(2, 100 + 1):
    cnt = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        prime_arr.append(i)