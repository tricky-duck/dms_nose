# -*- coding: utf-8 -*-
from random import randint, choice, randrange
from model.media import Media
from config import write_generated_data
from utils.string_util import random_string, random_string_fixed_len, random_string_mult
from utils.image_util import create_image
from utils.file_util import *

max_len = 50


# Возвращает рандомный объект
def create_random(test_name='media_random', prefix='', name=None, width=None, height=None,
                  file_type=None, progressive=None, file_path=None):
    if not name:
        name = random_string(prefix, max_len)
    if not width:
        width = randint(1, 100)
    if not height:
        height = randint(1, 100)
    if not file_type:
        file_type = ['JPG', 'JPEG', 'PNG', 'BMP']
    choose_type = choice(file_type)
    if not progressive:
        progressive = False
    if not file_path:
        file_path = (abs_path_to_file('../data/media/%s/%s' % (test_name, (name + '.' + choose_type))))
    return Media(name=name, width=width, height=height,
                 file_type=choose_type, progressive=progressive, file_path=file_path)


def test_generator(test_name, prefix, data_quantity):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media_list = []
    for i in range(data_quantity):
        media = Media()
        media.make_name_random(prefix)
        media.make_random_height()
        media.make_random_width()
        media.make_random_type()
        media.file_path = (abs_path_to_file('../data/media/%s/%s' % (test_name, (media.name + '.' + media.file_type))))
        create_image(media.file_path, media.width, media.height, media.progressive)
        media_list.append(media)
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# test_generator('media_test', 'Test_', 5)


# генератор заданного количества рандомных объектов медиа
# файлы создаются в заданной папке
# префикс используюеся в именах файлов
# если выставлен флаг modify имя объекта и имя файла будут отличаться
def media_generator_all_random(test_name, prefix, data_quantity, modify=False):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media_list = []
    for i in range(data_quantity):
        media = create_random(test_name, prefix)
        create_image(media.file_path, media.width, media.height, media.progressive)
        if modify:
            media = media.get_clone_with_other_name(random_string(prefix, max_len))
        media_list.append(media)
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# генератор заданного количества рандомных объектов медиа с настраивыми параметрами
# если выставлен флаг modify новое имя объекта будет фиксированной длины
def media_generator_fixed_params(test_name, prefix, data_quantity, name=None, mod_name=None, width=None, height=None, file_type=None,
                                 progressive=None, modify=False):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media_list = []
    for i in range(data_quantity):
        media = create_random(test_name, prefix, name=name, width=width, height=height, file_type=file_type, progressive=progressive)
        create_image(media.file_path, media.width, media.height, media.progressive)
        if modify:
            media = media.get_clone_with_other_name(mod_name)
        media_list.append(media)
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# генератор заданного количества рандомных объектов медиа с одинаковым рандомным именем
def media_generator_fixed_name(test_name, prefix, data_quantity):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media_list = []
    fixed_name = random_string(prefix, max_len)
    for i in range(data_quantity):
        media = create_random(test_name, prefix)
        create_image(media.file_path, media.width, media.height, media.progressive)
        media = media.get_clone_with_other_name(fixed_name)
        media_list.append(media)
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# генератор заданного количества рандомных объектов медиа именем именем из фиксированных символов
def media_generator_fixed_symbol(test_name, data_quantity, symbol):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media_list = []
    for i in range(data_quantity):
        name = random_string_mult(symbol, max_len)
        media = create_random(test_name, name=name)
        create_image(media.file_path, media.width, media.height, media.progressive)
        media_list.append(media)
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# генератор заданного количества экземпляров рандомного объекта
def media_generator_clone(test_name, prefix, data_quantity):
    update_dir(abs_path_to_file('../data/media/%s' % test_name))
    media = create_random(test_name, prefix)
    create_image(media.file_path, media.width, media.height, media.progressive)
    media_list = [media for x in range(0, data_quantity)]
    write_generated_data(abs_path_to_file('../data/%s.json' % test_name), media_list)


# # ПОЗИТИВНЫЕ ТЕСТЫ
#
# ~~~набор даннных для добавления без переименования
media_generator_all_random('media_positive', 'Pos_', 5)

# # ~~~набор даннных для добавления с переименованием
# media_generator_all_random('media_positive_mod', 'Mod_', 5, modify=True)
#
#
# # НЕГАТИВНЫЕ ТЕСТЫ
#
# # ~~~набор рандомных progressive JPG/JPEG
# media_generator_fixed_params('media_negative_progressive', 'Progr_', 2, file_type=['JPG', 'JPEG'], progressive=True)
#
# # ~~~набор рандомных BMP размером больше 2Мб
# media_generator_fixed_params('media_negative_file_size', 'Size_', 1, width=1000, height=1000, file_type=['BMP'])
#
# # ~~~набор рандомных данных некорректного формата
# media_generator_fixed_params('media_negative_file_type', 'Type_', 2, width=100, height=100, file_type=['GIF', 'TIFF'])
#
# # ~~~набор рандомных данных с именем длиной более 50 символов
# media_generator_fixed_params('media_negative_long_name', '', 1, name=random_string_fixed_len('Long55_', 55))
#
# # ~~~набор рандомных данных для добавления с переименованием имени в строку длиной более 50 символов
# media_generator_fixed_params('media_negative_long_name_mod', 'Long_', 1, mod_name=random_string_fixed_len('Long55_', 55), modify=True)
#
# # ~~~набор рандомных данных для добавления с переименованием имени в пустую строку
# media_generator_fixed_params('media_negative_empty_name', 'Empty_', 2, mod_name='', modify=True)
#
# # ~~~набор рандомных данных с именами из пробелов
# media_generator_fixed_symbol('media_negative_spaces', 2, ' ')
#
# # ~~~набор рандомных данных для добавления с переименованием имени в строку из пробелов
# media_generator_fixed_params('media_negative_spaces_mod', 'Space_', 2, mod_name=random_string_mult(' ', max_len), modify=True)
#
# # ~~~набор данных с одинаковыми именами но разными файлами
# media_generator_fixed_name('media_negative_fixed', 'Fixed_', 3)
#
# # ~~~набор данных для цикличного добавления одного и того же объекта
# media_generator_clone('media_negative_clone', 'Clone_', 3)
