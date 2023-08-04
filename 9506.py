while True:
    a = int(input())
    if a == -1:
        break
    else:
        l = []
        for i in range(1, a + 1):
            if a % i == 0 and a != i:
                l.append(i)
        l.sort()
        if a == sum(l):
            print(f'{a} = ', end='')
            for i in range(len(l)):
                print(f'{l[i]} ', end='')
                if len(l) - 1 == i:
                    print()
                else:
                    print('+', end=' ')
        else:
            print(f'{a} is NOT perfect.')