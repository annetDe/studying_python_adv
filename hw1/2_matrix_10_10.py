"""
Дана матрица целых чисел 10x10. Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число.
(либо рандом либо чтение из файла)
"""

from random import randint

lst = [[randint(10, 50) for i in range(10)] for j in range(10)]

num_str = ''
while not num_str.isdecimal() or 10 > int(num_str) or int(num_str) > 50:
    num_str = input('Enter number from 10 to 50: ')
    if num_str.isdecimal() and 10 <= int(num_str) <= 50:
        number = int(num_str)
    else:
        print('Conditions not met. Try again.')

for i in lst:
    print(i)

rows, cols = [], []
for i in range(10):
    for j in range(10):
        if lst[i][j] == number:
            rows.append(i)
            cols.append(j)

print('Rows (index): ', *rows)
print('Columns (index): ', *cols)
