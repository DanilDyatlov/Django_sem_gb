from random import choice, randint

GAME_TITLES = {
    'HT': 'Орел или Решка',  # heads_and_tails
    'RD': 'Бросок кубика',  # roll_the_dice
    'RN': 'Случайное число от 1 до 100',  # random_number
}


def get_results(game: str, tries: int) -> list[str]:
    result = []
    match game:
        case 'HT':
            result = [heads_and_tails() for _ in range(tries)]
        case 'RD':
            result = [roll_the_dice() for _ in range(tries)]
        case 'RN':
            result = [random_number() for _ in range(tries)]
    return result


def heads_and_tails() -> str:
    return f'{choice(["Орел", "Решка", ])}'


def roll_the_dice() -> str:
    return f'{randint(1, 6)}'


def random_number() -> str:
    return f'{randint(1, 100)}'