"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая будет принимать некоторое начальное целое число и
увеличивать его на 1 в бесконечном цикле. Если будет передано число, которое
больше 10, то кинуть ValueError. Функция должна вернуть количество произведенных
итераций (сколько раз она в цикле прибавляла 1)

ПРИМЕРЫ
--------------------------------------------------------------------------------
lets_break(1) -> 9
lets_break(-5) -> 15
lets_break(5) -> 5
lets_break(20) -> ValueError
"""


def lets_break(n: int) -> int:
    if n > 10:
        raise ValueError("Начальное значение больше 10")
    current_value = n
    counter = 0
    while True:
        counter += 1
        current_value += 1
        print(counter)
        if current_value == 10:
            break
    return counter


if __name__ == '__main__':
    assert lets_break(1) == 9
    assert lets_break(5) == 5
    assert lets_break(-20) == 30
    print('Решено!')
