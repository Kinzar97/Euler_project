def check_palindrome(a):
    a = list(str(a))
    i = 0
    while i < len(a) // 2:
        if a[i] != a[-i - 1]:
            return False
        i += 1
    return True


b = []
for j in range(100, 999):
    for i in range(100, 999):
        l = j * i
        if check_palindrome(l):
            b.append(l)
print(max(b))
