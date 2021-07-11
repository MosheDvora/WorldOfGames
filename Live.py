from GuessGame import play as guess_play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as currency_play
from Score import add_score


def welcome(name):
    print("hello " + name + ' and welcome to the World Of Games(WOG)\n'
                            'Here you can find many cool games to play\n')


def load_game():
    game_code = get_game_code_from_user()
    game_difficulty = get_game_difficulty_from_user()
    if game_code == 1:
        result = guess_play(game_difficulty)
    elif game_code == 2:
        result = memory_play(game_difficulty)
    else:
        result = currency_play(game_difficulty)
    if result:
        add_score(game_difficulty)
    else:
        return False


def get_game_code_from_user():
    game_code = -1
    while game_code == -1:
        game_code_input = input("Please choose a game to play:\n"
                                "1. Guess Game - guess a number and see if you chose like the computer\n"
                                "2. Memory Game - a sequence of numbers will appear for 1 second and you have to "
                                "guess it back\n"
                                "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        if game_code_input.isnumeric() and int(game_code_input) in range(0, 4):
            game_code = int(game_code_input)
            break
        else:
            game_code = -1
    return game_code


def get_game_difficulty_from_user():
    game_difficulty = -1
    while game_difficulty == -1:
        game_difficulty_input = input("Please choose game difficulty from 1 to 5:\n")
        if game_difficulty_input.isnumeric() and int(game_difficulty_input) in range(0, 6):
            game_difficulty = int(game_difficulty_input)
            break
        else:
            game_difficulty = -1
    return game_difficulty
