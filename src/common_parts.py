from enum import Enum


EXIT_FLAGS = ("e", "exit", "в", "выход", "выйти")


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2
