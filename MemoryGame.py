def generate_sequence(game_difficulty):
    from random import randint
    import time
    random_list_of_number = []
    for n in range(game_difficulty):
        random_list_of_number.append(randint(0, 101))
    print(random_list_of_number, end='')
    time.sleep(0.7)
    print("\r"" ")
    return random_list_of_number


def get_list_from_user(game_difficulty):
    from num2words import num2words
    user_guessed_list_number = []
    print("Enter the " + num2words(int(game_difficulty)) + " numbers that were on the screen")
    for n in range(game_difficulty):
        user_guessed_number = -1
        while user_guessed_number == -1:
            user_guessed_number = input("Enter the " + num2words(n + 1, ordinal=True) + "    ")
            if user_guessed_number.isnumeric() and int(user_guessed_number) in range(101):
                user_guessed_list_number.append(int(user_guessed_number))
                break
            else:
                print("You must enter a number and it must be in the range between 1-100")
                user_guessed_number = -1
    return user_guessed_list_number


def is_list_equal(random_list_of_number, user_guessed_list_number):
    print(random_list_of_number == user_guessed_list_number)


def play(game_difficulty):
    random_list_of_number = generate_sequence(game_difficulty)
    user_guessed_list_number = get_list_from_user(game_difficulty)
    return is_list_equal(random_list_of_number, user_guessed_list_number)
