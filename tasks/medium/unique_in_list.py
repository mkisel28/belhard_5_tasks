"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая проверит, все ли элементы в списке уникальны

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_unique([2, 1, 5, 4, 7]) -> True
is_unique([2, 1, 5, 4, 2]) -> False
"""


def is_unique(array: list) -> bool:
    unique = []
    for i in array:
        if i in unique:
            continue
        else:
            unique.append(i)
    if len(unique) == len(array):
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_unique([2, 1, 5, 4, 7])
    assert not is_unique([2, 1, 5, 4, 2])
    print('Решено!')
