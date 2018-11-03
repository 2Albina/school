b = []
a = input()

while a != '':
    b.append(int(a))
    a = input()
print(b)

c = []
a = input()

while a != '':
    c.append(int(a))
    a = input()
print(c)


def min_fun(b):
    min_num = b[0]
    for k in b:
        if min_num >= k:
            min_num = k
    print(min_num)

min_fun(b)
min_fun(c)

#school
