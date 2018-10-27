'''#решение 1 
a = int(input('enter year of birth \n'))
b = int(input('enter year of death \n'))
c = int(input('enter multiplicity \n'))
k = 0
while a <= b:
    if a % c == 0:
        k = k + 1
    a = a + 1
print(k)
'''

#решение 2
a = int(input('enter year of birth \n'))
b = int(input('enter year of death \n'))
c = int(input('enter multiplicity \n'))

i = 0
k = 0

while i <= b:
    if (i >= a) and (i <= b):
        k += 1
    i += c
print (k)


