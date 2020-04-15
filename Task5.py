def check_div_range1_20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


m = False
n = 20
while m != True:
    n += 20
    m = check_div_range1_20(n)
print(n)

