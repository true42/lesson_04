"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random


def generator(integer):
    '''
    Необходимо указать длину генератора

    Возвращет генератор со случайными числами
    '''
    for i in range(integer):
        yield int(random.random() * 100)


def chek_more(gener):
    '''
    Принимает список с числами

    Возвращает список значений исходного списка, которые были больше предыдущих
    '''
    test_list = []
    for el in range(1, len(gener)):
        if gener[el] > gener[el-1]:
            test_list.append(gener[el])
    return test_list


x = [el for el in generator(15)]
print(x)
print(chek_more(x))
