__author__ = 'anna.matveeva'

from test import *
from model.project import Project
from random import randrange
import time

def setup():
    global app
    app = set_app()

def test_delete_project():
    if app.project.count_projects() == 0:
        app.project.button_create()
        app.project.mheg_parameters(Project(branchName="mheg to delete"))
        app.project.button_submit_project_creation()
        app.project.button_create()
        app.project.stingray_parameters(Project(branchName="stingray to delete", appId="2", root="3", scope="4"))
        app.project.button_submit_project_creation()
    old_project_list = app.project.get_projects_list()
    index = randrange(len(old_project_list))
    app.project.delete_project_by_index(index)
    app.project.button_submit_deletion()
    app.alert.alert_project_deleted()
    time.sleep(0.5)
    new_project_list = app.project.get_projects_list()
    assert (len(old_project_list) - 1) == len(new_project_list)
    old_project_list[index:index+1] = []
    assert old_project_list == new_project_list


def test_cancel_project_deletion():
    if app.project.count_projects() == 0:
        app.project.button_create()
        app.project.mheg_parameters(Project(branchName="mheg to delete"))
        app.project.button_submit_project_creation()
        app.project.button_create()
        app.project.stingray_parameters(Project(branchName="stingray to delete", appId="2", root="3", scope="4"))
        app.project.button_submit_project_creation()
    old_project_list = app.project.get_projects_list()
    index = randrange(len(old_project_list))
    app.project.delete_project_by_index(index)
    app.project.button_cancel_deletion()
    time.sleep(0.5)
    new_project_list = app.project.get_projects_list()
    assert len(old_project_list) == len(new_project_list)


def test_delete_all_projects():
    if app.project.count_projects() == 0:
        app.project.button_create()
        app.project.mheg_parameters(Project(branchName="mheg to delete"))
        app.project.button_submit_project_creation()
        app.project.button_create()
        app.project.stingray_parameters(Project(branchName="stingray to delete", appId="2", root="3", scope="4"))
        app.project.button_submit_project_creation()
    while app.project.count_projects() > 0:
        old_project_list = app.project.get_projects_list()
        index = randrange(len(old_project_list))
        app.project.delete_project_by_index(index)
        app.project.button_submit_deletion()
        time.sleep(0.5)







