__author__ = 'anna.matveeva'

from test import *
from model.project import Project

from time import sleep
from random import randrange

def setup():
    global app
    app = set_app()


def test_edit_mheg_project_name():
    if app.project.count_mheg_projects() == 0:
        app.project.button_create()
        app.project.mheg_parameters(Project(branchName="mheg to edit"))
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    index = randrange(len(old_mheg_projects_list))
    sleep(1)
    app.project.edit_mheg_project_name_by_index(index)
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    assert len(old_mheg_projects_list) == len(new_mheg_projects_list)