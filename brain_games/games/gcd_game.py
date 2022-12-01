from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 60


def get_data():
    num1 = randint(LOWER_BOUND, UPPER_BOUND)
    num2 = randint(LOWER_BOUND, UPPER_BOUND)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)
