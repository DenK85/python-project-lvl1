from random import randint


DESCRIPTION = 'What number is missing in the progression?'
LOWER_BOUND = 1
UPPER_BOUND = 12
STEP_UPPER = 10
LOWER_LENGHT = 5
UPPER_LENGHT = 12



def get_data():
    start = randint(LOWER_BOUND, UPPER_BOUND)
    step = randint(LOWER_BOUND, STEP_UPPER)
    lenght = randint(LOWER_LENGHT, UPPER_LENGHT)
    progression = get_progression(start, step, lenght)
    correct_answer_index = randint(LOWER_BOUND, len(progression) - 1)
    correct_answer = str(progression[correct_answer_index])
    progression[correct_answer_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
    


def get_progression(start, step, lenght):
    end = start + (lenght * step)
    progression_list = []
    for num in range(start, end, step):
        progression_list.append(num)
    return progression_list
    
