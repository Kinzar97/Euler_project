a = [1, 2]
n = 0
sum = 0
for i in range(2, 4000000):
    if i == a[1 + n] + a[0 + n]:
        a.append(i)
        n += 1
for i in a:
    if i % 2 == 0:
        sum += i
print(sum)
