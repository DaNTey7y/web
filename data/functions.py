from random import choice
from PIL import Image


def generate_s(n):
    symbs = 'abcdefghijklmnopqrstuvwxyz0123456789'
    name = ''.join([choice(symbs) for i in range(9)])
    return name


def resize_image(path):
    im = Image.open(path)
    maxsize = (200, 200)
    im.thumbnail(maxsize, Image.ANTIALIAS)
    im.save(path)


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

