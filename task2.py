#2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random


def random_choice(list_var):
    if len(list_var) == 0:
        return None
    else:
        return random.choice(list_var)


if __name__ == '__main__':
    list1 = [8, 9, 10, 33, 44]
    list2 = []
    print(random_choice(list1))
    print(random_choice(list2))

