# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint 

n = int(input('Enter power  X '))

for i in range (n, -1, -1):
    coefficient = randint(-10,10)
    if coefficient != 0 and i != 0:
        if coefficient > 0:
            print(f' +{coefficient}*X**{i}', end = '')
        else:
            print(f' {coefficient}*X**{i}', end = '')
    if coefficient != 0 and i == 0:
        if coefficient > 0:
            print(f'+{coefficient} ', end = '')
        else:
            print(f'{coefficient} ', end = '')
print ('= 0')