def number_is_inrange(number, the_range):
    if number.isnumeric() and int(number) in range(0, the_range + 1):
        return True
    else:
        return False


def compare_results(secret_gen_number, user_guessed_number):
    return secret_gen_number == user_guessed_number


def generate_number(game_difficulty):
    from random import randint
    return randint(1, game_difficulty)


def get_guess_from_user(game_difficulty):
    user_guessed_number = -1
    while user_guessed_number == -1:
        user_guessed_number = input("Enter a number between: 1 and " + str(game_difficulty) + "\n")
        if number_is_inrange(user_guessed_number, game_difficulty):
            return int(user_guessed_number)
            break
        else:
            user_guessed_number = -1


def play(game_difficulty):
    return compare_results(generate_number(game_difficulty), get_guess_from_user(game_difficulty))

