from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 35


def get_data():
    operand_1 = randint(LOWER_BOUND, UPPER_BOUND)
    operand_2 = randint(LOWER_BOUND, UPPER_BOUND)
    operator = ['+', '-', '*']
    random_operator = choice(operator)
    question = f'{operand_1} {random_operator} {operand_2}'
    correct_answer = str(calc(operand_1, random_operator, operand_2))
    return question, correct_answer


def calc(operand_1, random_operator, operand_2):

    if random_operator == '+':
        result = operand_1 + operand_2
    elif random_operator == '-':
        result = operand_1 - operand_2
    elif random_operator == '*':
        result = operand_1 * operand_2
    return result
