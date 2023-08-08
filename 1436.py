a = int(input())
cnt = 0
num = 666
while True:
    if str(666) in str(num):
        cnt += 1
    if cnt == a:
        break
    num += 1
print(num)