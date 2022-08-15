'''
  В этом файле написан код, выполняющий то же самое,
  что и штатная (встроенная) функция map

  То есть, я смотрю, как работает сортировка с разными вариантами
'''

lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
print( sorted(lst, key=len) )


def check_sorted(iterable, funcSort=None, reverse=False):
    return sorted(iterable, key=funcSort, reverse=reverse)

print()
a=[1,4,5,6,3,2]
print('Список: ', a)
print(sorted(a))
print(check_sorted(a))
print(check_sorted(a, reverse=True))

print()
a=(1,4,5,6,3,2)
print('Кортеж: ', a)
print(sorted(a))
print(check_sorted(a))
print(check_sorted(a, reverse=True))

print()
lst = ['sd3', 'qqwed6', 'вакуитр8', 'фыв4', 'ь2', '1']
print(lst)
print(check_sorted(lst))
print(check_sorted(lst, reverse=True))

print()
lst = [2.0, 4.5, 7.9, 5, 6.42, 3.1, 1.25]
print(lst)
# Конструкция (x % 1) даёт остаток от деления на 1, то есть, извлекает дробную часть числа.
# Конструкция int((x % 1)*10) дробную часть числа умножает на 10 и округляет.
# То есть, в итоге должны получить только десячичный разряд.
#          [0, 5, 9, 0, 4, 1, 2]
# Идея взята тут:
# https://dvsemenov.ru/kak-izvlech-desyatichnuyu-chast-ili-drobnuyu-chast-chisla-v-python/
print(list(map(lambda x: int((x % 1)*10), lst)))
#          вар 1:  [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
print('вар 1: ', check_sorted(lst, funcSort=lambda x: int((x % 1)*10)))
#          вар 2:  [2, 4, 8, 5, 6, 3, 1]
print('вар 2: ', list(map(lambda x: round(x), lst)))
#          вар 3:  [2.0, 4.5, 7.9, 5, 6.4, 3.1, 1.2]
print('вар 3: ', list(map(lambda x: round(x, 1), lst)))
#          вар 4:  [0, 5, 9, 0, 4, 1, 2]
print('вар 4: ', list(map(lambda x: int((x % 1)*10), lst)))

print()
d = check_sorted(lst, funcSort=lambda x: int((x % 1) * 10)) #== [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
#          [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
print(d)

d = sorted(lst, key=lambda x: int((x % 1) * 10)) #== [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
#          [2.0, 5, 3.1, 1.25, 6.42, 4.5, 7.9]
print(d)

print()
str_val = 'Hello world'
#          вар 1:  [' ', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print('вар 1: ', check_sorted(str_val))
#          вар 2:  ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'e', 'd', 'H', ' ']
print('вар 2: ', check_sorted(str_val, reverse=True))
#          вар 3:  ['e', 'o', 'o', 'H', 'l', 'l', ' ', 'w', 'r', 'l', 'd']
print('вар 3: ', check_sorted(str_val, funcSort=lambda x: x not in 'qeyuioaj'))
#          вар 4:  ['e', 'o', 'o', 'H', 'l', 'l', ' ', 'w', 'r', 'l', 'd']
print('вар 4: ', sorted(str_val, key=lambda x: x not in 'qeyuioaj'))
