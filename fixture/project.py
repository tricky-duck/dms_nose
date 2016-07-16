# -*- coding: utf-8 -*-

import time
from model.project import Project
from fixture.alert import AlertHelper
from time import sleep

class ProjectHelper:

    def __init__(self, app):
        self.app = app
        self.alert = AlertHelper(app)

    def sleep(self):
        # just wait fo few seconds
        time.sleep(5)

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/header/nav/div[2]/ul[1]/li[1]/a").click()

    mheg_project_cache = None
    stingray_project_cache = None
    project_cache = None

####MHEG PROJECTS

    def mheg_parameters(self, project):
        wd = self.app.wd
        wd.find_element_by_id("branchName").click()
        wd.find_element_by_id("branchName").clear()
        wd.find_element_by_id("branchName").send_keys(project.branchName)
        wd.implicitly_wait(20)
        wd.find_element_by_css_selector(".form-group.templates .btn.btn-default.btn-radio .mheg").click()
        self.mheg_project_cache = None

    def mheg_project_create_positive(self, data):
        wd = self.app.wd
        self.button_create()
        self.mheg_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_project_saved()

    def mheg_project_create_empty_name(self, data):
        wd = self.app.wd
        self.button_create()
        self.mheg_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_specify_name()
        self.button_cancel_project_creation()

    def mheg_project_create_duplicate(self, data):
        wd = self.app.wd
        self.mheg_project_create_positive(data)
        self.alert.alert_project_saved()
        self.button_create()
        self.mheg_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_name_already_exist()
        self.button_cancel_project_creation()

    def count_mheg_projects(self):
        wd = self.app.wd
        try:
            mheg_list = len(wd.find_elements_by_xpath(".//*[@class='mheg']"))
        except:
            mheg_list = 0
        self.a = mheg_list
        return mheg_list

    def get_mheg_projects_list(self):
        if self.mheg_project_cache is None:
            wd = self.app.wd
            self.mheg_project_cache = []
            for element in wd.find_elements_by_xpath(".//*[@class='name'][preceding-sibling::span[@class='mheg']]"):
                text = element.get_attribute("title")
                self.mheg_project_cache.append(Project(branchName = text))
        return list(self.mheg_project_cache)


####STINGRAY PROJECTS

    def stingray_parameters(self, project):
        wd = self.app.wd
        wd.find_element_by_id("branchName").click()
        wd.find_element_by_id("branchName").clear()
        wd.find_element_by_id("branchName").send_keys(project.branchName)
        wd.find_element_by_xpath("//form[@class='editPage']/div[2]/div[1]/span").click()
        wd.find_element_by_id("appID").click()
        wd.find_element_by_id("appID").clear()
        wd.find_element_by_id("appID").send_keys(project.appId)
        wd.find_element_by_id("scope").click()
        wd.find_element_by_id("scope").clear()
        wd.find_element_by_id("scope").send_keys(project.scope)
        wd.find_element_by_id("root").click()
        wd.find_element_by_id("root").clear()
        wd.find_element_by_id("root").send_keys(project.root)
        self.stingray_project_cache = None

    def stingray_project_create_positive(self, data):
        wd = self.app.wd
        self.button_create()
        self.stingray_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_project_saved()

    def stingray_project_create_empty_name(self, data):
        self.button_create()
        self.stingray_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_specify_name()
        self.button_cancel_project_creation()

    def stingray_project_create_empty_appid(self, data):
        self.button_create()
        self.stingray_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_specify_appid()
        self.button_cancel_project_creation()

    def stingray_project_create_empty_scope(self, data):
        self.button_create()
        self.stingray_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_specify_scope()
        self.button_cancel_project_creation()

    def stingray_project_create_empty_root(self, data):
        self.button_create()
        self.stingray_parameters(data)
        self.button_submit_project_creation()
        self.alert.alert_specify_root()
        self.button_cancel_project_creation()

    def count_stingray_projects(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(".//*[@class='stingray']"))

    def get_stingray_projects_list(self):
        if self.stingray_project_cache is None:
            wd = self.app.wd
            self.stingray_project_cache = []
            for element in wd.find_elements_by_xpath(".//*[@class='name'][preceding-sibling::span[@class='stingray']]"):
                text = element.get_attribute("title")
                self.stingray_project_cache.append(Project(branchName = text))
        return list(self.stingray_project_cache)


    def delete_project_by_index(self, index):
        wd = self.app.wd
        time.sleep(1)
        wd.find_elements_by_xpath(".//*[@id='branches']/descendant::button")[index].click()
        wd.find_element_by_xpath(".//*[@class='pull-right open']//ul/li[4]").click()
        self.mheg_project_cache = None
        self.stingray_project_cache = None
        self.project_cache = None

    def edit_project_name_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(".//*[@class='normal']/span[@class='name']")[index].click()
        wd.find_element_by_xpath(".//*[@class=\"edit name form-control\"]").clear()
        wd.find_element_by_xpath(".//*[@id='branches']//input").send_keys("new name\n")
        self.mheg_project_cache = None
        self.stingray_project_cache = None


    def count_projects(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(".//*[@class='panel panel-default']"))

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_cache = []
            for element in wd.find_elements_by_xpath(".//*[@class='name']"):
                text = element.get_attribute("title")
                self.project_cache.append(Project(branchName = text))
        return list(self.project_cache)

####BUTTONS

#-----------------------------------------------------------------------------------------------------------PROJECT PAGE

    def button_create(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".btn.btn-success.pull-left.add").click()


#----------------------------------------------------------------------------------------------------CREATE PROJECT PAGE
    def button_submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@class='btn btn-success pull-right']").click()
        sleep(1)
        self.mheg_project_cache = None
        self.stingray_project_cache = None

    def button_cancel_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@class='btn btn-default pull-left']").click()
        self.mheg_project_cache = None
        self.stingray_project_cache = None

    def button_submit_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='Dialog-small']/div//button[1]").click()

    def button_cancel_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='Dialog-small']/div//button[2]").click()