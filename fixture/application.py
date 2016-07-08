__author__ = 'anna.matveeva'

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.alert import Alert
from fixture.button import Button

class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise  ValueError("Unrecognized browser %s" %browser)

        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.alert = Alert(self)
        self.button = Button(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.139.152")

    def destroy(self):
        self.wd.quit()
