# -*- coding: utf-8 -*-
from __future__ import print_function
from nose_config import *
#from nose import allure
from model.media import Media
from nose.tools import assert_equal
from nose_parameterized import parameterized, param


def setup_module():
    global app, db
    print('')
    print (__name__, 'setup_function()---')
    app = set_app()
    # db = set_db()


# ----POSITIVE--------------------------
# картинка в соотвествии с требованиями
#@allure.severity("high")
@parameterized([param(media_json) for media_json in loads_from_json("media_positive.json")])
def test_add_media(media_json):
    media = media_json
    old_media = app.media.media_get_list()
    alert_message = app.media.media_add_one_file_browse(media)
    new_media = app.media.media_get_list()
    old_media.append(media)
    v1 = sorted(old_media, key=Media.id_or_max)
    v2 = sorted(new_media, key=Media.id_or_max)
    assert_equal(v1, v2, 'Элемент добавлен')
    alert_text = loads_from_json("alerts.json")['add_one_file'].message
    assert_equal(alert_message, alert_text, 'Сообщение об успешном добавлении файла отображается')


# # картинка в соотвествии с требованиями через переименование
# @parameterized([param(media_json) for media_json in load_from_json("media_positive_mod.json")])
# def test_add_media_with_modify_name(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_with_rename(media)
#     new_media = app.media.media_get_list()
#     old_media.append(media)
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент добавлен и переименован')
#     alert_text = load_from_json("alerts.json")['add_one_file'].message
#     assert_equal(alert_message, alert_text, 'Сообщение об успешном добавлении файла отображается')
#
#
# # отмена добавления картинки
# @parameterized([param(media_json) for media_json in load_from_json("media_positive.json")])
# def test_cancel_add_media(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     visible = app.media.media_cancel_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     assert_equal(visible, False, 'Алерт не появился')
#
#
# # отмена выбора картинки
# def test_cancel_add_media_os():
#     old_media = app.media.media_get_list()
#     visible = app.media.media_cancel_add_file_browse_pyauto()
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     assert_equal(visible, False, 'Алерт не появился')
#
#
# # ----NEGATIVE--------------------------
# # progressive JPG/JPEG
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_progressive.json")])
# def test_add_media_progressive(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = ((load_from_json("alerts.json")['add_progressive_error']).message % (media.name + '.' + media.file_type))
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # картинка размером больше 2Мб
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_file_size.json")])
# def test_add_media_too_big_file(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = ((load_from_json("alerts.json")['add_file_size_error']).message % (media.name + '.' + media.file_type))
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # картинка некорректного формата
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_file_type.json")])
# def test_add_media_wrong_format(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = ((load_from_json("alerts.json")['add_file_format_error']).message % (media.name + '.' + media.file_type))
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# картинка с именем длиной больше 50 символов
#@allure.severity("medium")
@parameterized([param(media_json) for media_json in loads_from_json("media_negative_long_name.json")])
def test_add_media_name_too_long(media_json):
    media = media_json
    old_media = app.media.media_get_list()
    alert_message = app.media.media_add_one_file_browse(media)
    new_media = app.media.media_get_list()
    old_media.append(media.get_clone_with_other_name(media.name[:50]))
    v1 = sorted(old_media, key=Media.get_key)
    v2 = sorted(new_media, key=Media.get_key)
    assert_equal(v1, v2, 'Элемент добавлен с именем обрезанным до 50 символов')
    alert_text = loads_from_json("alerts.json")['add_one_file'].message
    assert_equal(alert_message, alert_text, 'Сообщение об успешном добавлении файла отображается')
#
#
# # картинка с именем длиной больше 50 символов через переименование
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_long_name_mod.json")])
# def test_add_media_with_modify_name_too_long(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_with_rename(media)
#     new_media = app.media.media_get_list()
#     old_media.append(media.get_clone_with_other_name(media.name[:50]))
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элемент добавлен с именем в 50 символов')
#     alert_text = load_from_json("alerts.json")['add_file_name_too_long_error'].message
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # картинка с именем длиной 0 символов через переименование
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_empty_name.json")])
# def test_add_media_with_modify_name_empty(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_with_rename(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = load_from_json("alerts.json")['add_file_name_empty'].message
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # картинка с именем из пробелов
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_spaces.json")])
# def test_add_media_name_spaces(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = load_from_json("alerts.json")['add_file_name_spaces'].message
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # картинка с именем из пробелов через переименование
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_spaces_mod.json")])
# def test_add_media_modify_name_spaces(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_with_rename(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элемент не добавлен')
#     alert_text = load_from_json("alerts.json")['add_file_name_spaces'].message
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об ошибке')
#
#
# # повторное добавление картинки
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_clone.json")])
# def test_add_one_existing_media_file(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_browse(media)
#     new_media = app.media.media_get_list()
#     unique_name = app.media.media_get_unique_name(media.name, sorted(old_media, key=Media.get_key))
#     old_media.append(media.get_clone_with_other_name(unique_name))
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'При совпадении имен новое имя индексируется')
#     alert_text = load_from_json("alerts.json")['add_one_file'].message
#     assert_equal(alert_message, alert_text, 'Сообщение об успешном добавлении файла отображается')
#
#
# # картинка имя которой уже используется
# @parameterized([param(media_json) for media_json in load_from_json("media_negative_fixed.json")])
# def test_add_one_existing_media_file_with_modify(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_message = app.media.media_add_one_file_with_rename(media)
#     new_media = app.media.media_get_list()
#     unique_name = app.media.media_get_unique_name(media.name, sorted(old_media, key=Media.get_key))
#     old_media.append(media.get_clone_with_other_name(unique_name))
#     v1 = sorted(old_media, key=Media.get_key)
#     v2 = sorted(new_media, key=Media.get_key)
#     assert_equal(v1, v2, 'При совпадении имен новое имя индексируется')
#     alert_text = load_from_json("alerts.json")['add_one_file'].message
#     assert_equal(alert_message, alert_text, 'Отображение сообщения об успешном добавлении файла')
