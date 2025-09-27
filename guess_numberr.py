from typing import Tuple


# def guess_number2(secret: int, low: int, high: int = 0) -> Tuple[int, int]:
#     '''
#     Поиск числа в диапазоне значений
#     :param secret: число, которое нужно угадать
#     :param low: нижняя граница диапазона
#     :param high: верхняя граница диапазона
#     :return:
#     Tuple[int, int]: угаданное число, кол-во попыток
#     '''
#     attempts = 0
#     for guess in range(low, high + 1):
#         attempts += 1
#         if guess == secret:
#             return guess, attempts
#     raise ValueError("Число не найдено")


def guess_number(secret: int, elements: list[int], algorithm="brute force") -> Tuple[int, int]:
    '''
    Поиск числа в диапазоне значений
    :param secret: число, которое нужно угадать
    :param elements: массив итерируемых чисел
    :param algorithm: алгоритм поиска
    :return:
    Tuple[int, int]: угаданное число, кол-во попыток
    '''
    attempts = 0

    if algorithm == "brute force":
        for guess in elements:
            attempts += 1
            if guess == secret:
                return guess, attempts
        raise ValueError("Число не найдено")

    elif algorithm == "binary":
        low = 0
        high = len(elements) - 1

        while low <= high:
            attempts += 1
            mid = (low + high) // 2
            guess = elements[mid]

            if guess == secret:
                return guess, attempts
            elif guess < secret:
                low = mid + 1
            else:
                high = mid - 1

        raise ValueError("Число не найдено")

    else:
        raise ValueError(f"Неизвестный алгоритм: {algorithm}")
