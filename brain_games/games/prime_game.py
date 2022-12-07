from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 50


def get_data():
    number = randint(LOWER_BOUND, UPPER_BOUND)

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False
    else:
        return True
