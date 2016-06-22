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
    time.sleep(0.5)     #необходимая задержка при наборе тестовых данных
    app.project.button_create()
    app.project.mheg_parameters(mheg_positive)
    app.project.button_submit_project_creation()
    app.alert.alert_project_saved()
    while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
        pass
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_positive)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName=""))),    #empty, min-1
    (param(Project(branchName=" "))),   #space
    (param(Project(branchName="   "))),   #multiple space
                ])
def test_create_mheg_project_negative(mheg_negative_empty):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)
    app.project.button_create()
    app.project.mheg_parameters(mheg_negative_empty)
    app.project.button_submit_project_creation()
    app.alert.alert_specify_name()
    app.project.button_cancel_project_creation()
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="duplicate name"))),
                ])
def test_create_mheg_project_negative(mheg_negative_exist):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)     #необходимая задержка при списке тестовых данных
    app.project.button_create()
    app.project.mheg_parameters(mheg_negative_exist)
    app.project.button_submit_project_creation()
    app.alert.alert_project_saved()
    while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
        pass
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_negative_exist)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)     #необходимая задержка при списке тестовых данных
    app.project.button_create()
    app.project.mheg_parameters(mheg_negative_exist)
    app.project.button_submit_project_creation()
    app.alert.alert_name_already_exist()
    app.project.button_cancel_project_creation()
    assert len(old_mheg_projects_list) == app.project.count_mheg_projects()
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


# @parameterized([
#     (param(Project(branchName="abcdefjhijklmnopqrstuvwxyzabcdefjhijklmnopqrstuvwxyzabcdefjhijklmno \
# pqrstuvwxyzabcdefjhijklmnopqrу100"))),    #max*2
#                 ])
# def test_create_mheg_project_negative(mheg_negative_maxlen):
#     old_mheg_projects_list = app.project.get_mheg_projects_list()
#     time.sleep(0.5)
#     app.project.button_create()
#     app.project.mheg_parameters(mheg_negative_maxlen)
#     app.project.submit_project_creation()
#     app.project.alert_max_len()
#     app.project.submit_project_creation()
#     while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
#         pass









# def teardown_module():
#     global app
#     app = stop_app()
#
# def teardown():
#     global app
#     app = stop_app()