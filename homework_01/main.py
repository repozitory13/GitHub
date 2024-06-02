"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    return list([nums ** 2 for nums in num])

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(nums):
    if nums <= 1:
        return False
    k = 0
    for i in range(2, nums // 2 + 1):
        if (nums % i == 0):
             k = k+1
    if k <= 0:
        return True
    else:
         return False

def filter_numbers(num, filter_type):
    if filter_type == ODD:
        return list(filter(lambda nums: nums % 2, num))
    else:
        pass
    if filter_type == EVEN:
        return list(filter(lambda nums: not nums % 2, num))
    else:
        pass
    if filter_type == PRIME:
        return list([nums for nums in num if is_prime(nums)])
    else:
        pass
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """