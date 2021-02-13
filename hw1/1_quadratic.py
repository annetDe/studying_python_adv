"""
Программа принимает от пользователя диапазоны для коэффициентов a, b, c квадратного уравнения: ax2 + bc + c = 0.
Перебирает все варианты целочисленных коэффициентов в указанных диапазонах, определяет квадратные уравнения, которые
имеют решение.
"""


def int_input(string):
    while True:
        try:
            tmp = int(input(f'Enter {string}: '))
        except ValueError:
            print(f'{string} must be a number. Try again.')
        else:
            break
    return tmp


def quadratic_with_solution(a_1, a_2, b_1, b_2, c_1, c_2):
    lst = []
    for a in range(a_1, a_2+1):
        if a == 0:
            continue
        for b in range(b_1, b_2+1):
            for c in range(c_1, c_2+1):
                d = b ** 2 - 4 * a * c
                if d < 0:
                    continue
                else:
                    x1 = (-b + d ** 0.5) / (2 * a)
                    x2 = (-b - d ** 0.5) / (2 * a)
                    lst.append([a, b, c, 'Yes', round(x1, 2), round(x2, 2)])
    return lst


a1 = int_input('a1')
a2 = int_input('a2')
b1 = int_input('b1')
b2 = int_input('b2')
c1 = int_input('c1')
c2 = int_input('c2')

res_list = quadratic_with_solution(a1, a2, b1, b2, c1, c2)

for i in res_list:
    print(*i)
print(f'There are {len(res_list)} quadratic with solution.')
