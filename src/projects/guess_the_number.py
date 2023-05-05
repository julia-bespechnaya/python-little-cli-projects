import random

from src.support_functions import get_random_number, get_difference_of_two_digits, is_prime


class GameGuessTheNumber:
    """ Игра Угадай число.
    Условие победы: пользователь вводит в консоль число, равное hidden_number.
    После каждой неверной попытки пользователь получает одну из подсказок, описанных в методе show_clue. """

    TITLE = "Угадай Число"

    DIFFICULTIES = ("easy", "medium", "hard")

    # В каком диапазоне будет загадано число в зависимости от сложности
    NUMBERS_RANGES = {"easy": (1, 10),
                      "medium": (1, 50),
                      "hard": (1, 100)}

    # Сколько очков отнимается при неверном ответе
    SCORE_PENALTIES = {"easy": 10,
                       "medium": 10,
                       "hard": 10}

    # Сколько очков выдается за угадывание числа в зависимости от сложности
    VICTORY_POINTS = {"easy": 50,
                      "medium": 75,
                      "hard": 100}

    # Hint rarity

    def __init__(self):
        self.show_greeting()

        self.user = self.init_user()
        self.difficulty = self.init_difficulty()

        self.numbers_range = self.NUMBERS_RANGES[self.difficulty]
        self.score_penalty = self.SCORE_PENALTIES[self.difficulty]
        self.victory_points = self.VICTORY_POINTS[self.difficulty]

        self.start_game()

    def start_game(self):
        while True:
            self.play_match()
            str_in = input("Нажмите enter, чтобы попробовать еще раз.\n"
                           "Введите c (change), чтобы выбрать другой уровень сложности.\n"
                           "Введите e (exit), чтобы выйти.\n")
            if str_in.lower() in ("e", "exit", "в", "выход", "выйти"):
                break

        print("\nСпасибо за игру!\n")

    def play_match(self):
        print(f"\nСчет игрока {self.user.login}: {self.user.score}\n")

        hidden_number = get_random_number(*self.numbers_range)
        input_number = self.get_input_number(*self.numbers_range)

        hint_manager = HintManager(hidden_number)

        while input_number != hidden_number:
            self.user.score = self.user.score - self.score_penalty if self.user.score > self.score_penalty else 0
            print(f"Вы не угадали! Счет: {self.user.score}\n")

            hint_manager.show_hint(input_number)
            input_number = self.get_input_number(*self.numbers_range)

        self.user.score += self.victory_points
        print(f"Вы угадали! Счет: {self.user.score}\n")

    @staticmethod
    def get_input_number(min_num, max_num):
        str_in = input(f"Попробуйте угадать целое число "
                       f"от {min_num} "
                       f"до {max_num}: ")

        """ Обработка ошибок """
        while not str_in.isdigit():
            str_in = input("Повторите ввод: ")

        return int(str_in)

    @classmethod
    def show_greeting(cls):
        print(f"Игра \"{cls.TITLE}\"\n")

    @staticmethod
    def init_user():
        # TODO: Подключить БД
        str_in = input("Чтобы играть за гостевой аккаунт, нажмите Enter.\n"
                       "Чтобы создать или зайти в свой аккаунт, введите логин: ")
        print()

        return User(str_in if str_in else "Guest")

    @classmethod
    def init_difficulty(cls):
        str_in = input("Выберите уровень сложности:\n"
                       "1. Легко\n2. Нормально\n3. Сложно\n"
                       "Введите номер сложности: ")

        # Обработка ошибок
        while str_in not in ("1", "2", "3"):
            str_in = input("Повторите ввод: ")

        return cls.DIFFICULTIES[int(str_in) - 1]


class HintManager:

    HINTS_4_ANY = ("is_smaller", "multiples")
    HINTS_4_TWO_DIGIT = ("two_digits_diff", )
    HINTS_4_TREE_DIGIT = ("", )
    HINT_TYPES = HINTS_4_ANY + HINTS_4_TWO_DIGIT + HINTS_4_TREE_DIGIT
    # Оценивается в число
    HINT_RARITY = {}

    def __init__(self, hidden_number):
        self.hidden_number = hidden_number
        self.hints = self.init_hints(hidden_number)
        self.hints_availability = dict.fromkeys(self.HINT_TYPES, True)
        self.dividers = (i for i in range(2, hidden_number)
                         if hidden_number % i == 0)

    def show_hint(self, input_number):

        hint_type = self.choose_hint()

        if hint_type == "is_smaller":
            print("Искомое число меньше" if input_number > self.hidden_number else "Искомое число больше")

        if hint_type == "multiples":
            if is_prime(self.hidden_number):
                print("Искомое число является простым")
                self.hints_availability[hint_type] = False
            else:
                try:
                    divider = next(self.dividers)
                    print(f"Искомое число делится на {divider} без остатка")
                except StopIteration:
                    print("Все делители числа были перечислены")
                    self.hints_availability[hint_type] = False

        if hint_type == "two_digits_diff":
            difference = get_difference_of_two_digits(self.hidden_number)
            print(f"Разница между цифрами искомого числа составляет {difference}")
            self.hints_availability[hint_type] = False

    def choose_hint(self):
        hint_type = random.choice(self.hints)
        while not self.hints_availability[hint_type]:
            hint_type = random.choice(self.hints)
        return hint_type

    @classmethod
    def init_hints(cls, hidden_number):
        hints = cls.HINTS_4_ANY
        if 9 < hidden_number < 100:
            hints += cls.HINTS_4_TWO_DIGIT
        elif hidden_number > 100:
            hints += cls.HINTS_4_TREE_DIGIT
        return hints


class User:

    def __init__(self, login):
        self.login = login
        # TODO: доставать score и stats из БД
        self.score = 1000
        self.stats = {"first try win": 0}


def main():
    GameGuessTheNumber()


if __name__ == '__main__':
    main()


