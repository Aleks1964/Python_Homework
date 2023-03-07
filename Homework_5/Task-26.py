# * Задача 26: *
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def A_degree_B(a, b):
    if b == 0:
        return 1
    return A_degree_B(a, b-1) * a

A = int(input(f'Введите первое число '))
B = int(input(f'Введите второе число '))

print(f'{A} в степени {B} равно {A_degree_B(A, B)}.')
print(f'A = {A}; B = {B} -> {A_degree_B(A, B)} ({A}**{B})')