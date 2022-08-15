# Задание.
#
# 2. В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше


from m01_functions import *


# тесты для встроенных функций filter, map, sorted

def test_filter():
    lst = [1, 2.0, 3.1, 4, 5, 6, 7.9]
    assert check_filter(lambda x: x > 4, lst) == [5, 6, 7.9]
    lst = ['sd3', 'qqwed6', 'вакуитр8', 'фыв4', 'ь2', '1']
    assert check_filter(lambda x: len(x) < 4, lst) == ['sd3', 'ь2', '1']


def test_map():
    # можно проверить работу функции, если кол-во последовательностей
    # не совпадает с количеством аргументов функции.
    # Вопрос, как это сделать

    # проверяем, как функция работает с последовательностью в виде списка
    lst = ['apple6', 'banana7', 'cherry7']
    assert check_map(len, lst) == [6, 7, 7]
    # проверяем, как функция работает с последовательностью в виде кортежа
    tpl = ('apple6', 'banana7', 'cherry7')
    assert check_map(len, tpl) == [6, 7, 7]


def test_sorted():
    # проверяем работу на списке с числами
    lst = [4.5, 1.25, 2.0, 7.9, 6.42, 3.1, 5]
    assert check_sorted(lst) == [1.25, 2.0, 3.1, 4.5, 5, 6.42, 7.9]
    assert check_sorted(lst, reverse=True) == [7.9, 6.42, 5, 4.5, 3.1, 2.0, 1.25]
    assert check_sorted(lst, funcSort=lambda x: int((x % 1) * 10)) == [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
    # проверяем работу на списке из строк
    lst = ['sd3', 'qqwed6', 'вакуитр8', 'фыв4', 'ь2', '1']
    assert check_sorted(lst) == ['1', 'qqwed6', 'sd3', 'вакуитр8', 'фыв4', 'ь2']
    assert check_sorted(lst, funcSort=len) == ['1', 'ь2', 'sd3', 'фыв4', 'qqwed6', 'вакуитр8']
    assert check_sorted(lst, funcSort=len, reverse=True) == ['вакуитр8', 'qqwed6', 'фыв4', 'sd3', 'ь2', '1']

    # проверяем работу на кортеже с числами
    tpl = [4.5, 1.25, 2.0, 7.9, 6.42, 3.1, 5]
    assert check_sorted(tpl) == [1.25, 2.0, 3.1, 4.5, 5, 6.42, 7.9]
    assert check_sorted(tpl, reverse=True) == [7.9, 6.42, 5, 4.5, 3.1, 2.0, 1.25]
    assert check_sorted(tpl, funcSort=lambda x: int((x % 1) * 10)) == [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
    # проверяем работу на кортеже из строк
    tpl = ['sd3', 'qqwed6', 'вакуитр8', 'фыв4', 'ь2', '1']
    assert check_sorted(tpl, funcSort=len) == ['1', 'ь2', 'sd3', 'фыв4', 'qqwed6', 'вакуитр8']
    assert check_sorted(tpl, funcSort=len, reverse=True) == ['вакуитр8', 'qqwed6', 'фыв4', 'sd3', 'ь2', '1']

    # проверяем работу на строке
    str_val = 'Hello world'
    assert check_sorted(str_val) == [' ', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
    assert check_sorted(str_val, reverse=True) == ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'e', 'd', 'H', ' ']
        # Вытаскиваем сначала все гласные, потом согласные буквы
        # lambda-функция преобразовывает все буквы в значения 0
        # (если находится в строке 'qeyuioaj')
        # и 1, если символ не находится в строке 'qeyuioaj'.
        # И далее символы, соответствующие нулю выхосятся в начало
        # в том порядке, в каком они находились в исходной строке
    assert check_sorted(str_val, funcSort=lambda x: x not in 'qeyuioaj') == ['e', 'o', 'o', 'H', 'l', 'l', ' ', 'w', 'r', 'l', 'd']


# тесты для функций из библиотеки math: pi, sqrt, pow, hypot



def test_sqrt():
    assert check_sqrt(4) == 2.0


def test_pow():
    assert check_pow(2, 3) == 8


def test_hypot():
    assert check_hypot(3, 4) == 5


def test_pi():
    # Питон даёт такое значение pi: 3.141592653589793
    # Делаем тесты на получение числа pi с количеством знаков
    # после запятой меньше 15 (это проверяется, что что-то выдаёт).
    # Проверяем на граничном значении в 15 знаков и проверяем
    # на значении более 15 знаков - должно выдать те же самые 15 знаков

    # Преобразуем все отрицательные значения параметра точности в ноль
    # и возвращаем 3.0:
    # - для отрицательного значения параметра точность
    # - для параметра точность, равного нулю

    # Если точность (кол-во знаков) запрашивается больше 15,
    # то выдаём только 15 знаков после запятой
    assert check_pi(0) == 3.0
    assert check_pi(-2) == 3.0
    assert check_pi(3) == 3.142
    assert check_pi(15) == 3.141592653589793
    assert check_pi(16) == 3.141592653589793
