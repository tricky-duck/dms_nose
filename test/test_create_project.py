__author__ = 'anna.matveeva'

from nose_parameterized import parameterized, param
from model.project import Project
from test import *
import time

def setup():
    global app
    app = set_app()


@parameterized([
    (param(Project(branchName="branchname7"))),
    (param(Project(branchName="branchname8"))),
                ])
def test_create_mheg_project_positive(mheg_positive):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)
    app.project.button_create()
    app.project.mheg_parameters(mheg_positive)
    while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
        pass
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_positive)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="branchname1"))),
    (param(Project(branchName="branchname2"))),
                ])
def test_create_mheg_project_negative(mheg_negative):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)
    app.project.button_create()
    app.project.mheg_parameters(mheg_negative)
    while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
        pass
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_negative)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))







# def teardown_module():
#     global app
#     app = stop_app()
#
# def teardown():
#     global app
#     app = stop_app()