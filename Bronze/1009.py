# import sys;
count = int(input())

# for i in range(count):
#    a, b = map(int, sys.stdin.readline().rstrip().split())
#    result = a**b % 10
#    print(result)
for i in range(count):
    a, b = map(int, input().split())
    result = 1
    for j in range(b):
        result *= a
        if result >= 10:
            result = result % 10
            continue
    if result == 0:
        print(10)
    else:
        print(result)
