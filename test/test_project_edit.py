# -*- coding: utf-8 -*-

from test import *
from model.project import Project
from random import randrange

def setup():
    global app
    app = set_app()


def test_edit_project_name():
    if app.project.count_projects() == 0:
        app.project.mheg_project_create_positive(Project(branchName="mheg to edit"))
        app.project.stingray_project_create_positive(Project(branchName="stingray to edit", appId="2", root="3", scope="4"))
    old_projects_list = app.project.get_projects_list()
    index = randrange(len(old_projects_list))
    app.project.edit_project_name_by_index(index,"edited")
    new_projects_list = app.project.get_projects_list()
    assert len(old_projects_list) == len(new_projects_list)