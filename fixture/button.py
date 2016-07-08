from time import sleep

class Button:

    def __init__(self, app):
        self.app = app

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
