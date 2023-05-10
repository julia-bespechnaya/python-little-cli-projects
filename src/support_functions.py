import math
import random


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


def get_random_number(min_num, max_num):
    return random.randint(min_num, max_num)


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True

