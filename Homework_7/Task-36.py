# *Задача 36:*
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y)` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def print_operation_table(operation, num_rows, num_columns, start_row, start_column):
    for i in range(start_row, num_rows + start_row):
        for j in range(start_column, num_columns + start_column):
            print(operation(i, j), end='\t')
        print()

num_rows = int(input('Введите число строк: '))
num_columns = int(input('Введите число столбцов: '))
operation_type = input('Введите тип операции ("+" или "*"): ')

if operation_type == '+':
    operation = lambda i, j: i + j
    start_row = 0
    start_column = 0
elif operation_type == '*':
    operation = lambda i, j: i * j
    start_row = 1
    start_column = 1
else:
    print('Некорректный тип операции')
    exit()

print_operation_table(operation, num_rows, num_columns, start_row, start_column)