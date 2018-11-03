b = []
x = []
a = input()

while a != '':
    b.append(int(a))
    a = input()
print(b)
'''
i = 0
while i < len(b):
    if b[i] % 3 == 0:
        x.append(b[i])
    i = i + 1
print(x)'''

for i in b:
    if i % 3 == 0:
        x.append(i)
        
'''
k = 0
min_num = x[0]
while k < len(x):
    if min_num >= x[k]:
        min_num = x[k]
    k = k + 1
print(min_num)'''

min_num = x[0]
for k in x:
    if min_num >= k:
        min_num = k
print(min_num)


