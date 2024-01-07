a, b = map(int, input().split())
dic_name = {}
dic_idx = {}
problem = {}
for i in range(a):
    pocketM = input()
    dic_name[i + 1] = pocketM
    dic_idx[pocketM] = i + 1

for i in range(b):
    problem[i] = input()
    if problem[i].isdigit():
        print(dic_name.get(int(problem[i])))
    else:
        print(dic_idx.get(problem[i]))