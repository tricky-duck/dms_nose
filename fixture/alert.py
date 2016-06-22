__author__ = 'anna.matveeva'



class Alert:

    def __init__(self, app):
        self.app = app

# Msg           PROJECT PAGE

    def alert_project_saved(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg']//div[text()='Your project has been saved']")

    def alert_project_deleted(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg']//div[text()='Branch delete complete']")


# Msg-normal    CREATE PROJECT PAGE

    def alert_specify_name(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*/div[@id=\"msg-normal\"]//div[text()='Specify project name.']")


    def alert_max_len(self):
        wd =self.app.wd
        wd.find_element_by_xpath(".//*/div[@id=\"msg-normal\"]//div[text()='Maximum name length is 50.']")


    def alert_name_already_exist(self):
        wd =self.app.wd
        wd.find_element_by_xpath(".//*[@id='msg-normal']/div/div[text()=\"Name must be unique for the projects of the same type.\"]")
