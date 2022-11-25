import prompt


def welcome_user():
    """Asks for the user name."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
