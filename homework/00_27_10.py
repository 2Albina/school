'''
#задача 1

import random
a = str(random.randint(99, 999))
print(a, int(a[0]) + int(a[1]) + int(a[2]))


#задача 2 (1 вариант)

a = int(input('enter number \n'))
if a < 10:
    print('1 разряд')
elif a > 9 and a < 100:
    print('2 разрядa')
elif a > 99 and a < 1000:
    print('3 разрядa')
elif a > 999 and a < 10000:
    print('4 разрядa')
elif a > 9999 and a < 100000:
    print('5 разрядa')
    
#задача 2 (2 вариант)
a = input('enter number \n')
print(len(a))'''

#задача 3 (3 вариант)

a = abs(int(input('enter number \n')))
k = 0
while a > 0:
    a = a // 10
    k = k + 1
print(k)

'''
#задача 3

a = int(input('enter year \n'))
if a%4 == 0 and a % 100 !=0 or a%400 == 0:
    print('year is leap')
else:
    print('year is not leap')'''
