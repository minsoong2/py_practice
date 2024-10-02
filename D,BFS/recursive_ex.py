def recursive_fun(i):
    if i == 5:
        return

    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_fun(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

# recursive_fun(1)

def recursive_fact(n):
    if n <= 1:
        return 1

    return n * recursive_fact(n - 1)