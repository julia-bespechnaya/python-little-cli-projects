import math
import random
import time


def get_num_len(num):
    abs_num = abs(num)
    return int(math.log10(abs_num)) + 1 if abs_num > 0 else 1


# Возвращает цифры в обратном порядке (i = 0 вернет последнюю цифру числа)
def get_digit(number, i):
    return number // 10 ** i % 10


def get_digits(number):
    return [get_digit(number, i) for i in range(len(str(number)))][::-1]


def get_difference_of_two_digits(number):
    digits = get_digits(number)
    return abs(digits[0] - digits[1])


# current_range представляет из себя tuple из двух чисел
def get_random_number(current_range):
    min_num, max_num = current_range

    num4seed = time.localtime().tm_min + time.localtime().tm_sec
    random.seed(num4seed)

    return random.randint(min_num, max_num - 1)


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
        return True

