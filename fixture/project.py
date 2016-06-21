__author__ = 'anna.matveeva'
import time
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("html/body/header/nav/div[2]/ul[1]/li[1]/a").click()

    def button_create(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".btn.btn-success.pull-left.add").click()

    def submit_project_creation(self, wd):
        wd.find_element_by_css_selector(".modal-footer .btn.btn-success.pull-right").click()
        self.mheg_project_cache = None
        self.stingray_project_cache = None


    def sleep(self):
        # just wait fo few seconds
        time.sleep(5)

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
        self.submit_project_creation(wd)

    def mheg_parameters(self, project):
        wd = self.app.wd
        wd.find_element_by_id("branchName").click()
        wd.find_element_by_id("branchName").clear()
        wd.find_element_by_id("branchName").send_keys(project.branchName)
        wd.implicitly_wait(20)
        wd.find_element_by_css_selector(".form-group.templates .btn.btn-default.btn-radio .mheg").click()
        self.submit_project_creation(wd)

    def delete_project_by_index(self, index):
        wd = self.app.wd
        #self.select_project_by_index(index)
        #wd.find_element_by_css_selector("#branches").click()
        # submit deletion
        time.sleep(1)
        wd.find_elements_by_xpath(".//*[@id='branches']/descendant::button")[index].click()
        wd.find_element_by_xpath(".//*[@class='pull-right open']//ul/li[4]").click()
        wd.find_element_by_xpath(".//*[@id='Dialog-small']/div//button[1]").click()
        self.mheg_project_cache = None
        self.stingray_project_cache = None

    def edit_mheg_project_name_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(".//*[@class='name'][preceding-sibling::span[@class='mheg']]")[index].click()
        wd.find_element_by_xpath(".//*[@class=\"edit name form-control\"]").clear()
        wd.find_element_by_xpath(".//*[@id='branches']//input").send_keys("new name\n")
        self.mheg_project_cache = None
        self.stingray_project_cache = None

    def count_mheg_projects(self):
        wd = self.app.wd
        try:
            mheg_list = len(wd.find_elements_by_xpath(".//*[@class='mheg']"))
        except:
            mheg_list = 0
        self.a = mheg_list
        return mheg_list

    def count_stingray_projects(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(".//*[@class='stingray']"))

    mheg_project_cache = None

    def get_mheg_projects_list(self):
        if self.mheg_project_cache is None:
            wd = self.app.wd
            self.mheg_project_cache = []
            for element in wd.find_elements_by_xpath(".//*[@class='name'][preceding-sibling::span[@class='mheg']]"):
                text = element.get_attribute("title")
                self.mheg_project_cache.append(Project(branchName = text))
        return list(self.mheg_project_cache)

    stingray_project_cache = None

    def get_stingray_projects_list(self):
        if self.stingray_project_cache is None:
            wd = self.app.wd
            self.stingray_project_cache = []
            for element in wd.find_elements_by_xpath(".//*[@class='name'][preceding-sibling::span[@class='stingray']]"):
                text = element.get_attribute("title")
                self.stingray_project_cache.append(Project(branchName = text))
        return list(self.stingray_project_cache)

