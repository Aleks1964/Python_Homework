# * Задача 16: *
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

import sys
N = int(input(f'Введите число элементов массива '))
massiv = [int(i) for i in input('Введите через пробел целые числа - элементы массива: ').split()]
count = 0
if N != len(massiv):
    print('Введённый Вами массив не соответствует введённому ранее количеству элементов массива.')
    sys.exit()
else:   
    X = int(input(f'Введите искомое в массиве число '))
    for i in massiv:
	    if i == X:
		    count += 1
if count == 0:
    print(f'Число {X} НЕ встречается в массиве {massiv}.')
else:
    print(f'-> {count}')
    print(f'Число {X} встречается в массиве {massiv} {count} раза.')