"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)


print(my_func(12, 11, 10))