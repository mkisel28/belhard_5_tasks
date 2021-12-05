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
    longest = text[-1]
    for i in text:
        if (len(i) > len(longest)):
            longest = i
    counter = collections.Counter(text).most_common()[0][0]
    return counter, longest


if __name__ == '__main__':
    assert common_and_longest("привет пока ялюблюpython привет") == ('привет', 'ялюблюpython')
    print('Решено!')
