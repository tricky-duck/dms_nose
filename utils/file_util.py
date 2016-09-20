# -*- coding: utf-8 -*-
import os
import shutil


def abs_path_to_file(relative_path):
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))


def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def delete_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def update_dir(path):
    delete_dir(abs_path_to_file(path))
    check_dir(abs_path_to_file(path))
