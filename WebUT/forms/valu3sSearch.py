from .form import *

class Valu3sSearch(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.searchInput = "//form[@id='searchGadget_form']/div/input"
        self.submitElement = "//form[@id='searchGadget_form']/div/input[@type='submit']"
    
    def fill_in(self, value):
        self.driver.find_element_by_xpath(self.searchInput).send_keys(value)
