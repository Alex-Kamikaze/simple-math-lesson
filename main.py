def add(a: int | float, b: int | float) -> int | float:
    """
    Складывает два числа

    Args:
        a (int | float): Первое число
        b (int | float): Второе число

    Returns:
        out (int | float): Итоговое число
    """
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    """
    Вычитает два числа

    Args:
        a (int | float): Первое число
        b (int | float): Второе число

    Returns:
        out (int | float): Итоговое число
    """
    return a - b


def mul(a: int | float, b: int | float) -> int | float:
    """
    Перемножает два числа

    Args:
        a (int | float): Первое число
        b (int | float): Второе число

    Returns:
        out (int | float): Итоговое число
    """
    return a * b


def div(a: int | float, b: int | float) -> int | float:
    """
    Делит два числа

    Args:
        a (int | float): Первое число
        b (int | float): Второе число

    Returns:
        out (int | float): Итоговое число

    Raises:
        ZeroDivisionError: Если число b является 0
    """
    return a / b
