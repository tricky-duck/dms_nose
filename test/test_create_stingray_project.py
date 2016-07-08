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
    app.button.button_create()
    app.project.stingray_parameters(stingray_positive)
    app.button.button_submit_project_creation()
    while not len(old_stingray_projects_list) + 1 == app.project.count_stingray_projects():
        pass
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    old_stingray_projects_list.append(stingray_positive)
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="", appId="appId3", scope="scope3", root="root3"))),
    (param(Project(branchName=" ", appId="appId4", scope="scope4", root="root4"))),
    (param(Project(branchName="   ", appId="appId4", scope="scope4", root="root4"))),
                ])
def test_create_stingray_project_empty_name(stingray_empty_name):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.button.button_create()
    app.project.stingray_parameters(stingray_empty_name)
    app.button.button_submit_project_creation()
    app.alert.alert_specify_name()
    app.button.button_cancel_project_creation()
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="stingray5", appId="", scope="scope5", root="root5"))),
    (param(Project(branchName="stingray6", appId=" ", scope="scope6", root="root6"))),
    (param(Project(branchName="stingray7", appId="    ", scope="scope7", root="root7"))),
                ])
def test_create_stingray_project_empty_appID(stingray_empty_appID):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.button.button_create()
    app.project.stingray_parameters(stingray_empty_appID)
    app.button.button_submit_project_creation()
    app.alert.alert_specify_appid()
    app.button.button_cancel_project_creation()
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="stingray8", appId="appId8", scope="", root="root8"))),
    (param(Project(branchName="stingray9", appId="appId9", scope=" ", root="root9"))),
    (param(Project(branchName="stingray10", appId="appId10", scope="   ", root="root10"))),
                ])
def test_create_stingray_project_empty_scope(stingray_empty_scope):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.button.button_create()
    app.project.stingray_parameters(stingray_empty_scope)
    app.button.button_submit_project_creation()
    app.alert.alert_specify_scope()
    app.button.button_cancel_project_creation()
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([
    (param(Project(branchName="stingray11", appId="appId11", scope="scope11", root=""))),
    (param(Project(branchName="stingray12", appId="appId12", scope="scope12", root=" "))),
    (param(Project(branchName="stingray13", appId="appId13", scope="scope13", root="   "))),
                ])
def test_create_stingray_project_empty_root(stingray_empty_root):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.button.button_create()
    app.project.stingray_parameters(stingray_empty_root)
    app.button.button_submit_project_creation()
    app.alert.alert_specify_root()
    app.button.button_cancel_project_creation()
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))