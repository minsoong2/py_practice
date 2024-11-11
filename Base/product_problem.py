from itertools import product


def solution(word):
    answer = 0
    char_list = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, len(char_list) + 1):
        words.append(list(product(char_list, repeat=i)))

    re = []
    for l in words:
        re.append([str("".join(map(str, tup))) for tup in l])

    words_list = []
    for l in re:
        for w in l:
            words_list.append(w)
    words_list.sort()
    print(words_list)

    for i in range(len(words_list)):
        if words_list[i] == word:
            answer = i + 1

    return answer