"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая принимает список целых чисел и возвращает минимальное

Нельзя пользоваться функциями sorted, list.sort, min, max

ПРИМЕРЫ
--------------------------------------------------------------------------------
min_in_list([1, 2, 3, -2, 3, 5]) -> -2
min_in_list([7, 2, 4, 6, 1, 4]) -> 1
"""


def min_in_list(some_list: list) -> int:
    answer = some_list.pop()
    for i in some_list:
        if i < answer:
            answer = i
    print(answer)
    return answer
    return answer


if __name__ == '__main__':
    assert min_in_list([1, -1, 5, 7, -2, 4]) == -2
    print('Решено!')
