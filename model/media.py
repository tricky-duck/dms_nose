# -*- coding: utf-8 -*-
from sys import maxsize
from random import randint, choice, randrange
from utils.string_util import random_string, random_string_fixed_len, random_string_mult

max_len = 50


class Media:

    def __init__(self, id=None, name=None, width=None, height=None, file_type=None, progressive=None, file_path=None):
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.file_type = file_type
        self.progressive = progressive
        self.file_path = file_path

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.file_type, self.width, self.height)

    def __eq__(self, other):
        return (self.name == other.name and str(self.width) == str(other.width) and
                str(self.height) == str(other.height) and
                (self.file_type is None or other.file_type is None or self.file_type == other.file_type))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def get_key(self):
        return self.name

    # Возвращает представление объекта с имзененным именем
    def get_clone_with_other_name(self, new_name):
        return Media(id=self.id, name=new_name, width=self.width, height=self.height,
                     file_type=self.file_type, progressive=self.progressive, file_path=self.file_path)

    # ГЕНЕРАТОР
    def make_name_random(self, prefix):
        self.name = random_string(prefix, max_len)
        return self.name

    def make_random_width(self, min_width=1, max_width=100):
        self.width = randint(min_width, max_width)
        return self.width

    def make_random_height(self, min_height=1, max_height=100):
        self.height = randint(min_height, max_height)
        return self.height

    def make_random_type(self, type_list=['JPG', 'JPEG', 'PNG', 'BMP']):
        self.file_type = choice(type_list)
        return self.file_type

    def make_progressive(self):
        self.progressive = True
        return self.progressive

    def set_type(self, file_type):
        self.file_type = file_type
        return self.file_type

