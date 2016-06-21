__author__ = 'anna.matveeva'

from nose_parameterized import parameterized, param
from model.project import Project
from test import *
import time

def setup():
    global app
    app = set_app()


@parameterized([
    (param(Project(branchName="stingray1", appId="appId1", scope="scope1", root="root1"))),
    (param(Project(branchName="stingray2", appId="appId2", scope="scope2", root="root2"))),
                ])
def test_create_stingray_project_positive(stingray_positive):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.button_create()
    app.project.stingray_parameters(stingray_positive)
    app.project.submit_project_creation()
    while not len(old_stingray_projects_list) + 1 == app.project.count_stingray_projects():
        pass
    new_stingray_projects_list = app.project.get_mheg_projects_list()
    old_stingray_projects_list.append(stingray_positive)
    # assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


#
# @parameterized([
#     (param(Project(branchName="mhegBr3", appId="appId3", scope="scope3", root="root3"))),
#     (param(Project(branchName="mhegBr4", appId="appId4", scope="scope4", root="root4"))),
#                 ])
# def test_create_stingray_project_negative(stingray_negative):
#     old_stingray_projects_list = app.project.get_stingray_projects_list()
#     time.sleep(0.5)
#     app.project.button_create()
#     app.project.stingray_parameters(stingray_negative)
#     while not len(old_stingray_projects_list) + 1 == app.project.count_stingray_projects():
#         pass
#     new_stingray_projects_list = app.project.get_mheg_projects_list()
#     old_stingray_projects_list.append(stingray_negative)
#     assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))
#
#

# def teardown_module():
#     global app
#     app = stop_app()
#
# def teardown():
#     global app
#     app = stop_app()