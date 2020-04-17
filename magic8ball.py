import random
def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain.'
    elif answer_number == 2:
        return 'It is decidedly so.'
    elif answer_number == 3:
        return 'You are in for a world of pain.'
    elif answer_number == 4:
        return 'Hello, Darkness - my old friend!'
    elif answer_number == 5:
        return 'Naan veezhven endru ninaithayo.'
    elif answer_number == 6:
        return 'Just do it!'
    elif answer_number == 7:
        return 'Gomma Vainko'
    elif answer_number == 8:
        return 'Ettu la sani!'
    elif answer_number == 9:
        return 'Ombodheyy.'

r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)
