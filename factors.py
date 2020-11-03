"""
Факторизация методом ро-Полларда.
Функция определения следующего члена поседовательности: F(x) = x ** 2 - x
x(n+1) = F(x(n))mod N
Использована вариация алгоритма, предложенная Флойдом.
"""

from itertools import count
from math import gcd
from sympy import isprime
from numpy import prod


def rho_pollard(number):
    x = 5
    # непосредственно функция
    def f(x):
        return (x ** 2 - x) % number
    # первый индекс - cycle - номер итерации
    for cycle in count(1):
        y = x
        #второй индекс - i = 2^cycle
        for i in range(2 ** cycle):
            x = f(x)
            factor = gcd(x - y, number)
            if factor > 1:
                return factor


numb = int(input('Enter number for factorization: '))
factors = []
d = 1
while not isprime(numb) and numb != 1:
    d = rho_pollard(numb)
    factors.append(d)
    numb = int(numb / d)
if numb != 1:
    factors.append((numb))
print(f"Factor's list: {factors}")
print(prod(factors))