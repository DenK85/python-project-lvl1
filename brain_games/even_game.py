from random import randint


def is_even(random_number):
    return random_number % 2 == 0


def get_answer():
    random_number = randint(1, 100)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number

    return correct_answer, question
