# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.alert import AlertHelper
from fixture.media import MediaHelper
from utils.wrapper import AllHelper


class Application:

    def __init__(self, browser, baseUrl, width, height):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise  ValueError("Unrecognized browser %s" %browser)
        self.wd.set_window_size(width, height)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.media = MediaHelper(self)
        self.wrapper = AllHelper(self)
        self.base_url = baseUrl
        self.alert = AlertHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
