# -*- coding: utf-8 -*-

from nose_parameterized import parameterized, param
from model.project import Project
from test import *
import time

def setup():
    global app
    app = set_app()


@parameterized([param(Project(**positive)) for positive in loads_from_json('project_create.json')['mheg_positive']])
def test_mheg_project_create_positive(mheg_positive):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    sleep(0.5)
    app.project.mheg_project_create_positive(mheg_positive)
    while not len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects():
        pass
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_positive)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**empty_name)) for empty_name in loads_from_json('project_create.json')['mheg_empty_name']])
def test_mheg_project_create_negative_empty_name(mheg_negative_empty):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    time.sleep(0.5)
    app.project.mheg_project_create_empty_name(mheg_negative_empty)
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))


@parameterized([param(Project(**duplicate)) for duplicate in loads_from_json('project_create.json')['mheg_duplicate']])
def test_mheg_project_create_negative_already_exist(mheg_negative_duplicate):
    old_mheg_projects_list = app.project.get_mheg_projects_list()
    app.project.mheg_project_create_duplicate(mheg_negative_duplicate)
    assert len(old_mheg_projects_list) + 1 == app.project.count_mheg_projects()
    new_mheg_projects_list = app.project.get_mheg_projects_list()
    old_mheg_projects_list.append(mheg_negative_duplicate)
    assert sorted(old_mheg_projects_list, key =(lambda x: x.branchName)) == sorted(new_mheg_projects_list,key = (lambda x: x.branchName))

