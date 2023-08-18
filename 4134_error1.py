import sys
import sympy

# prime_number_list = list(sympy.primerange(l[0], l[-1]))
num = int(sys.stdin.readline())
l = []
for i in range(num):
    l.append(int(sys.stdin.readline()))
for i in range(len(l)):
    if i+1 == len(l):
        break
    prime_num_l = list(sympy.primerange(l[i], l[i+1]))
    print(min(prime_num_l))
i = 1
a = l[len(l) - 1]
while True:
    a += i
    prime_num_l = list(sympy.primerange(l[len(l) - 1], a))
    if len(prime_num_l) > 0:
        print(min(prime_num_l))
        break