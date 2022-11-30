import prompt
from brain_games.games.even_game import DESCRIPTION
from brain_games.games.even_game import get_data


def logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)

    for round in range(1, 4):
        question, correct_answer = get_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
