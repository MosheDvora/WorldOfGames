from random import randint
import currency_converter


def get_money_interval(difficulty):
    from requests import ConnectionError
    try:
        c = currency_converter.CurrencyConverter()
        currency_rate = c.convert(1, 'USD', 'ILS')
    except ConnectionError as exc:
        raise Exception('Unable to get Currency ') from exc
    random_amount = randint(1, 101)
    low_level_point = round((currency_rate * random_amount) - (5 - difficulty), 2)
    high_level_point = round((currency_rate * random_amount) + (5 - difficulty), 2)
    return low_level_point, high_level_point


def get_guess_from_user():
    user_guessed_number = -1
    while user_guessed_number == -1:
        user_guessed_number = input("Currency Roulette - try and guess the value of a random amount of USD in ILS:  ")
        if user_guessed_number.isnumeric():
            return user_guessed_number
            break
        else:
            print("You must enter a number")
            user_guessed_number = -1


def play(difficulty):
    low, high = get_money_interval(difficulty)
    guessed_number_from_user = float(get_guess_from_user())
    return low >= guessed_number_from_user >= high
