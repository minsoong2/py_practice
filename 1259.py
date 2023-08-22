
def palindrome(s):
    arr = list(s)
    for i in range(len(s)):
        if arr[i] != arr[len(s) - i - 1]:
            return False
    return True

while True:
    s = input()
    if s == "0":
        break
    TF = palindrome(s)
    if TF:
        print("yes")
    else:
        print("no")
