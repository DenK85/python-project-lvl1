from random import randint


DESCRIPTION = 'Answer "yes" if number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_data():
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number

    return question, correct_answer


def is_even(random_number):
    return random_number % 2 == 0
