import sys
sys.path.append("..")

from ..forms.logInForm import *

from .subpage import *


class HomePageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.logInForm = LogInForm(driver)
        self.listLoggedInElements = "//div[@id='faceted-results']/div/table/tbody/tr"

    def get_list_of_elements(self):
        return self.driver.find_elements_by_xpath(self.listLoggedInElements)

    def get_testcase_by_name(self, name):
        els = self.get_list_of_elements()
        for el in els:
            text = el.get_attribute("innerText")
            if "Test Case" in text and name in text:
                return el
        return None

    def get_evaluation_scenario_by_name(self, name):
        els = self.get_list_of_elements()
        for el in els:
            text = el.get_attribute("innerText")
            if "Evaluation Scenario" in text and name in text:
                return el
        return None

    def get_requirement_by_name(self, name):
        els = self.get_list_of_elements()
        for el in els:
            text = el.get_attribute("innerText")
            if "Requirement" in text and name in text:
                return el
        return None


    def get_clickable_element_from_element(self, el):
        return el.find_element_by_tag_name("a")