from .form import *

class LogInForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.nameInput = "//div[@id='login-form']/form/div/div/div/input[@type='text']"
        self.passwordInput = "//div[@id='login-form']/form/div/div/div/input[@id='__ac_password']"
        self.submitElement = "//input[@id='buttons-login']"
        self.closeButton = "//a[@class='plone-modal-close']"
    
    def fill_in(self, name, password):
        self.driver.find_element_by_xpath(self.nameInput).send_keys(name)
        self.driver.find_element_by_xpath(self.passwordInput).send_keys(password)

    def close(self):
        try:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.closeButton))
        except(Exception):
            pass
