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


# POSITIVE
@nose.allure.severity("small")
@parameterized([param(media_json) for media_json in load_from_json("media_positive.json")])
def test_search_media_by_name(media_json):
    media = media_json
    old_media = app.media.media_get_results_of_search_by_text(media.name)
    new_media = app.media.media_search_by_name(media.name)
    v1 = sorted(old_media, key=Media.id_or_max)
    v2 = sorted(new_media, key=Media.id_or_max)
    assert_equal(v1, v2, 'Элемент найден')

