# -*- coding: utf-8 -*-

# from model.alert import Alert
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class AlertHelper:

    def __init__(self, app):
        self.app = app

# Msg           PROJECT PAGE

    def alert_project_saved(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg']//div[text()='Your project has been saved']")

    def alert_project_deleted(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg']//div[text()='Branch delete complete']")

    def alert_branch_changed(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg']//div[text()='Branch changed']")

# Msg-normal    CREATE PROJECT PAGE

    def alert_specify_name(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']//div[text()='Specify project name.']")

    def alert_specify_appid(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']//div[text()='Specify project application ID.']")

    def alert_specify_scope(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']//div[text()='Specify Scope.']")

    def alert_specify_root(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']//div[text()='Specify Root.']")

    def alert_max_len(self):
        wd =self.app.wd
        wd.find_element_by_xpath(".//*/div[@id=\"msg-normal\"]//div[text()='Maximum name length is 50.']")

    def alert_name_already_exist(self):
        wd =self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']/div/div[text()=\"Name must be unique for the projects of the same type.\"]")

#Media

    def get_media_message_text(self):
        wd = self.app.wd
        if self.is_visible('//*[@id="msg"]/div/div'):
            text = wd.find_element_by_xpath('//*[@id="msg"]/div/div').text
            if self.is_not_visible('//*[@id="msg"]/div/div'):
                return text


    def get_media_popup_text(self):
        wd = self.app.wd
        if self.is_visible('//*[@id="Dialog-small"]/div/div[2]/div[1]/h5'):
            return wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[1]/h5').text


    @staticmethod
    def long_name_parser(name):
        if len(name) < 15:
            name = '«' + name + '»'
            return name
        else:
            return name[:14] + '...'


    def is_visible(self, locator, timeout=3):
        wd = self.app.wd
        try:
            ui.WebDriverWait(wd, timeout).until(ec.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False


    def is_not_visible(self, locator, timeout=10):
        wd = self.app.wd
        try:
            ui.WebDriverWait(wd, timeout).until_not(ec.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
