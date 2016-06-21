__author__ = 'anna.matveeva'

from test import *
from model.project import Project
from random import randrange
import time

def setup():
    global app
    app = set_app()


def test_delete_project():
    if app.project.count_mheg_projects() == 0:
        app.project.button_create()
        app.project.mheg_parameters(Project(branchName="mheg2"))
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    index = randrange(len(old_mheg_projects_list))
    app.project.delete_project_by_index(index)
    time.sleep(2)
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    assert len(old_mheg_projects_list) - 1 == len(new_mheg_projects_list)
    old_mheg_projects_list[index:index+1] = []
    assert old_mheg_projects_list == new_mheg_projects_list



