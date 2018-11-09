x = list()
z = list()
a = input()

while a != '':
    x.append(int(a))
    a = input()
print(x)

for i in x:
    if i % 10 == 5:
        z.append(i)
print(z)

print(max(z))
