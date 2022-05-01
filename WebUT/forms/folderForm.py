from .form import *

class FolderForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IDublinCore-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IDublinCore-description']"

    def fill_in(self, title, summary):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
