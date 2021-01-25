# 1.1
a = "aaaa bbbb cccc AAAA BBBB CCCC"
b = len(a.split())
print(b)

# 1.2
a = "aaaa bbbb cccc AAAA BBBB CCCC"
for i in a.split():
    if i.startswith("a"):
        print(i)
for k in a.split():
    if k.startswith("A"):
        print(k)

# 2.1
a = 10
b = [1, 13, 5, 10, 9, 20, 25, 100]
for i in range(0, len(b)):
    if b[i] > a:
        print(b[i])

# 2.2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[0]
c = a[-1]
print(b, c)