# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class AllHelper:

    def __init__(self, app):
        self.app = app

    def click_if_visible(self, locator, timeout=3):
        wd = self.app.wd
        try:
            ui.WebDriverWait(wd, timeout).until(ec.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            print('Element not visible', TimeoutException)
        wd.find_element_by_xpath(locator).click()
