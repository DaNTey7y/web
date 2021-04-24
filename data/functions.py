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
