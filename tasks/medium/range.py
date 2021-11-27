"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию list_compose, которая принимает два списка (INDEX_LIST, VALUE_LIST).
Составить новый список: берем индекс из списка индексов, и вставляем значение по этому
индексу из другого списка. Если значения нет, что вставить None

ПРИМЕРЫ
--------------------------------------------------------------------------------
list_compose(INDEX_LIST, VALUE_LIST) -> ['b', 'f', None, None, 'c', 'd', None, 'e']
"""
INDEX_LIST = [1, -1, 6, -12, 2, 3, 9, 4]
VALUE_LIST = ['a', 'b', 'c', 'd', 'e', 'f']


def list_compose(indexes: list, values: list) -> list:
    list = []
    k = 0
    val_len = len(values)
    for i in indexes:
        k += 1
        if i > (val_len - 1) or i < (val_len - val_len - 1):
            list.append(None)
        else:
            list.insert(k, values[i])
    return list


if __name__ == '__main__':
    assert list_compose(INDEX_LIST, VALUE_LIST) == ['b', 'f', None, None, 'c', 'd',
                                                    None, 'e']
    print('Решено!')
