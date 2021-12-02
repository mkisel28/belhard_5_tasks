"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""

import collections


def common_and_longest(text: str) -> tuple:
    text = text.split()
    longest = max(text, key=len)
    counter = max(text, key=text.count)
    return counter, longest


if __name__ == '__main__':
    assert common_and_longest("привет пока ялюблюpython привет") == ('привет', 'ялюблюpython')
    print('Решено!')
