# -*- coding: utf-8 -*-

from nose_parameterized import parameterized, param
from model.project import Project
from test import *
import time


def setup():
    global app
    app = set_app()


@parameterized([param(Project(**positive))for positive in loads_from_json('project_create.json')['stingray_positive']])
def test_create_stingray_project_positive(stingray_positive):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.stingray_project_create_positive(stingray_positive)
    while not len(old_stingray_projects_list) + 1 == app.project.count_stingray_projects():
        pass
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    old_stingray_projects_list.append(stingray_positive)
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**empty_name)) for empty_name in loads_from_json('project_create.json')['stingray_empty_name']])
def test_stingray_project_create_negative_empty_name(stingray_empty_name):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.stingray_project_create_empty_name(stingray_empty_name)
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**empty_appid)) for empty_appid in loads_from_json('project_create.json')['stingray_empty_appid']])
def test_stingray_project_create_negative_empty_appID(stingray_empty_appID):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.stingray_project_create_empty_appid(stingray_empty_appID)
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**empty_scope)) for empty_scope in loads_from_json('project_create.json')['stingray_empty_scope']])
def test_create_stingray_project_empty_scope(stingray_empty_scope):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.stingray_project_create_empty_scope(stingray_empty_scope)
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**empty_root)) for empty_root in loads_from_json('project_create.json')['stingray_empty_root']])
def test_create_stingray_project_empty_root(stingray_empty_root):
    old_stingray_projects_list = app.project.get_stingray_projects_list()
    time.sleep(0.5)
    app.project.stingray_project_create_empty_root(stingray_empty_root)
    new_stingray_projects_list = app.project.get_stingray_projects_list()
    assert sorted(old_stingray_projects_list, key =(lambda x: x.branchName)) == sorted(new_stingray_projects_list,key = (lambda x: x.branchName))