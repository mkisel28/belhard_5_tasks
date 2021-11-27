def is_divide_by(to_divide: int, divider_1: int, divider_2: int) -> bool:
    result = None
    if (to_divide % divider_1 == 0 and to_divide % divider_2 == 0):
        result = True
        return result

    else:
        result = False
        return result


if __name__ == '__main__':
    td_val = int(input('Введите число для проверки: '))
    d_1_val = int(input('Введите первый делитель: '))
    d_2_val = int(input('Введите второй делитель: '))
    print(f"Число делится на 2 делителя: "
          f"{'да' if is_divide_by(td_val, d_1_val, d_2_val) else 'нет'}")
