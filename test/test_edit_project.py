__author__ = 'anna.matveeva'

from test import *
from model.project import Project
from random import randrange

def setup():
    global app
    app = set_app()


def test_edit_project_name():
    if app.project.count_projects() == 0:
        app.button.button_create()
        app.project.mheg_parameters(Project(branchName="mheg to edit"))
        app.button.button_submit_project_creation()
        app.button.button_create()
        app.project.stingray_parameters(Project(branchName="stingray to edit", appId="2", root="3", scope="4"))
        app.button.button_submit_project_creation()
    old_projects_list = app.project.get_projects_list()
    index = randrange(len(old_projects_list))
    app.project.edit_project_name_by_index(index)
    new_projects_list = app.project.get_projects_list()
    assert len(old_projects_list) == len(new_projects_list)