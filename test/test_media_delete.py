# -*- coding: utf-8 -*-
from __future__ import print_function
from config import *
from model.media import Media
from nose.tools import assert_equal
from nose_parameterized import parameterized, param


def setup_module():
    global app, db
    print('')
    print (__name__, 'setup_function()---')
    app = set_app()
    # db = set_db()


# # ----POSITIVE--------------------------
# удаление одного рандомного элемента
# def test_delete_one_media_file():
#     old_media = app.media.media_get_list()
#     alert_text = app.media.media_delete_one_file_random_without_select()
#     new_media = app.media.media_get_list()
#     old_media.remove(alert_text[0])
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элемент удален')
#     alert = load_from_json("alerts.json")
#     tt = alert_text[0].name
#     alert_message = (alert['delete_one_file'].message % alert_text[0].name)
#     assert_equal(alert_message, alert_text[1], 'Сообщение об успешном удалении файла отображается')


# # удаление нескольких рандомных элементов
# def test_delete_several_media_files(number=3):
#     old_media = app.media.media_get_list()
#     alert_text = app.media.media_delete_number_of_files_with_random_select(number)
#     new_media = app.media.media_get_list()
#     old_media = [x for x in old_media if x not in alert_text[0]]
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элементы удалены')
#     alert = load_from_json("alerts.json")
#     alert_message = (alert['delete_many_files'].message % number)
#     assert_equal(alert_message, alert_text[2], 'Сообщение об успешном удалении файлов отображается')


# удаление всех файлов через выбор нескольких рандомных элементов
# def test_delete_all_media_files(number=2):
#     media_count = len(app.media.media_get_list())
#     alert_text = app.media.media_delete_all_files(number)
#     new_media = app.media.media_get_list()
#     assert_equal(new_media, [], 'Все элементы удалены')
#     alert = load_from_json("alerts.json")
#     alert_message = (alert['delete_many_files'].message % media_count)
#     assert_equal(alert_message, alert_text[1], 'Сообщение об успешном удалении файлов отображается')


# # отмена удаления одного элемента
# @parameterized([param(media_json) for media_json in load_from_json("media_positive.json")])
# def test_cancel_delete_one_media_file(media_json):
#     media = media_json
#     old_media = app.media.media_get_list()
#     alert_visible = app.media.media_cancel_delete_one_file_without_select(media)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элементы не удалены')
#     assert_equal(alert_visible, False, 'Сообщение не отображается')
#
#
# # отмена удаления нескольких рандомных элементов
# def test_cancel_delete_number_of_media_files(number=2):
#     old_media = app.media.media_get_list()
#     alert_visible = app.media.media_cancel_delete_number_of_files_random_select(number)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элементы не удалены')
#     assert_equal(alert_visible, False, 'Сообщение не отображается')
#
#
# # отмена удаления всех элементов
# def test_cancel_delete_all_media_files(number=2):
#     old_media = app.media.media_get_list()
#     alert_visible = app.media.media_cancel_delete_all_files(number)
#     new_media = app.media.media_get_list()
#     v1 = sorted(old_media, key=Media.id_or_max)
#     v2 = sorted(new_media, key=Media.id_or_max)
#     assert_equal(v1, v2, 'Элементы не удалены')
#     assert_equal(alert_visible, False, 'Сообщение не отображается')
