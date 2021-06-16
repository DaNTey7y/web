from random import choice


def generate_s(n):
    symbs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    name = ''.join([choice(symbs) for i in range(9)])
    return name


def form_text(text, n):
    new_text = ''
    counter = 0
    for symb in text:
        if counter >= n:
            new_text += '\n'
            counter = 0
        new_text += symb
        counter += 1
    return new_text

