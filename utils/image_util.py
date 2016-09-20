# -*- coding: utf-8 -*-
from PIL import Image


def create_image(name, width, height, progressive):
    im = Image.new('RGBA', (width, height), 'blue')
    if progressive:
        im.save(name, progressive=True)
    else:
        im.save(name)
