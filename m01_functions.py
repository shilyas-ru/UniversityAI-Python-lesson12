'''
В этом файле написаны:
- функции для тестирования встроенных функций filter, map, sorted;
- функции для тестирования функций из библиотеки math: pi, sqrt, pow, hypot

Файл используется в "test_python_m01_functions.py" - через оператор
    from m01_functions import *
'''

from math import pi, sqrt, pow, hypot


# написанные функции для тестирования встроенных функций filter, map, sorted
def check_filter(func, iterable):
    '''
    Заготовка для теста для функции filter
    :param func: функция, которая принимает элемент фильтруемого
            объекта и должна вернуть bool значение
    :param iterable: последовательность или объект поддерживающий итерирование
    :return: отфильтрованная последовательность
    '''
    return list(filter(func, iterable))


def check_map(func, iterable):
    '''
    Заготовка для теста для функции filter
    :param func: пользовательская функция, вызывается для каждого элемента iterable
             функция должна принимать столько аргументов, сколько
             последовательностей передается в функцию map()
    :param iterable: последовательность или объект, поддерживающий итерирование.
             - Если передаются несколько иттераторов, то iterable инициализируется
             кортежем, собержащим все переданные последовательности.
             - Если последовательностей несколько, то пользовательская функция
             func должна принимать количество аргументов, соответствующее количеству
             переданных последовательностей, при этом function будет применяться к
             элементам из всех итераций параллельно.
             - При использовании нескольких последовательностей, функция map()
             останавливается, когда исчерпывается самая короткая итерация.
             Пример:
                 x = [1, 2, 3]
                 y = [4, 5, 6, 7]
                 # вычисление при помощи встроенной функции 'pow()'
                 # 'x' в степени 'y' для каждого элемента 2-х списков
                 list(map(pow, x, y))
             Вывод кода из примера:
                 [1, 32, 729]
             Пояснение:
                 pow(1, 4) == 1
                 pow(2, 5) == 32
                 pow(3, 6) == 729
    :return: объект итератора
    '''
    return list(map(func, iterable))


def check_sorted(iterable, funcSort=None, reverse=False):
    return sorted(iterable, key=funcSort, reverse=reverse)


# написанные функции для тестирования функций из библиотеки math: pi, sqrt, pow, hypot
def check_sqrt(num):
    '''
    Заготовка для теста для функции math.sqrt
    :param num: Число для которого вычисляется функция math.sqrt
    :return:
    '''
    return sqrt(num)


def check_pow(num, power):
    '''
    Заготовка для теста для функции math.pow
    :param num: Число котороt возводится в степень
    :param power: Значение степени
    :return: число num в степени power
    '''
    return pow(num, power)


def check_hypot(sideX, sideY):
    '''
    Заготовка для теста для функции math.hypot
    math.hypot(sideX, sideY) - вычисляет гипотенузу
    треугольника с катетами X и Y (math.sqrt(x * x + y * y)).
    :param sideX: Длина катета 1 в треугольнике
    :param sideY: Длина катета 2 в треугольнике
    :return: длина гипотенузы треугольника с катетами sideX и sideY
    '''
    return hypot(sideX, sideY)


def check_pi(accuracy):
    '''
    Заготовка для теста для значения math.pi
    :param accuracy: количество знаков после запятой,
           которые требуется оставить
    :return: число Пи (3.141592653589793), округлённое
           до заданного количества знаков после запятой
    '''
    # Преобразуем все отрицательные значения параметра точности в ноль
    accuracy = max(0, accuracy)
    # Если точность (кол-во знаков) запрашивается больше 15,
    # то выдаём только 15 знаков после запятой
    accuracy = min(accuracy, 15)
    return round(pi, accuracy)


if __name__ == '__main__':
    print('check_filter:', check_filter(lambda x: x > 4, [1, 2.0, 3.1, 4, 5, 6, 7.9]))
    print('check_filter:', check_filter(lambda x: len(x) < 4, ['sd3', 'qqwed6', 'вакуитр8', 'фыв4', 'ь2', '1']))
    print('check_map:', check_map(len, ('apple6', 'banana7', 'cherry7')))
    print('check_sqrt:', check_sqrt(4))
    print('check_pow:', check_pow(2, 3))
    print('check_hypot:', check_hypot(3, 4))
    print('check_pi:', check_pi(-2))
    print('check_pi:', check_pi(10))
    print('check_pi:', check_pi(16))
