"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""


def common_and_longest(text: str) -> tuple:
    text = text.split()
    longeest = text[0]
    times = 0
    times_temp = 0
    z = -1
    for i in text:
        if i != text[0]:
            if (len(i) > len(longeest)):
                longeest = i
    for i in text:
        z += 1
        if times_temp < text.count(i):
            times = text[z]
            times_temp = text.count(i)
    return times, longeest


if __name__ == '__main__':
    assert common_and_longest("привет пока ялюблюpython привет") == ('привет', 'ялюблюpython')
    print('Решено!')
