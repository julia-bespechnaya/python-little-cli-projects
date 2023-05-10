import sys

from projects.guess_the_number import GameGuessTheNumber

games = [GameGuessTheNumber]


def main():
    while True:
        print("Доступные игры и приложения:")
        print(*(f"{i + 1}. {games[i].TITLE}\n" for i in range(len(games))), sep="")

        game_number = get_game_number()
        # Start chosen game
        games[game_number - 1]()


def get_game_number():
    str_in = input("Введите номер, чтобы выбрать игру, "
                   "или введите e (exit), чтобы выйти: ")
    print()
    while True:
        try:
            game_number = int(str_in)
            if 1 <= game_number <= len(games):
                return game_number
        except ValueError:
            if str_in in ("e", "exit", "выход", "выйти"):
                sys.exit()
        str_in = input("Некорректное значение. Повторите ввод: ")


if __name__ == '__main__':
    main()







