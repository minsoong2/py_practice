while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a > b:
        for i in range(1, a+1):
            num = b * i
            if num == a:
                print('multiple')
                break
            elif i == a:
                print('neither')
                break
    if a < b:
        for i in range(1, b+1):
            num = a * i
            if num == b:
                print('factor')
                break
            elif i == b:
                print('neither')
                break