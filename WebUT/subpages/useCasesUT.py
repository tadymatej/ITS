from time import sleep
from .subpage import *

class UseCasesPageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.useCasesListElements = "//div[@id='faceted-results']/div/article"
        self.useCasesListLoggedInElements = "//div[@id='faceted-results']/div/table/tbody/tr"
        self.letterFilterXpathStart = "//span[@class='faceted_letter'"

    def filter_by_first_character(self, char):
        el = self.driver.find_element_by_xpath(self.letterFilterXpathStart + " and contains(text(), '" + char + "')]")
        self.driver.execute_script("arguments[0].click()", el)
        sleep(1)

    def get_use_cases_list(self):
        use_cases = self.driver.find_elements_by_xpath(self.useCasesListElements)
        if(len(use_cases) == 0):
            return self.driver.find_elements_by_xpath(self.useCasesListLoggedInElements)
        else:
            return use_cases

    def find_use_case_by_name(self, name):
        use_cases = self.get_use_cases_list()
        for use_case in use_cases:
            try:
                use_case.find_element_by_link_text(name)
                return use_case
            except(Exception):
                pass
        
        raise Exception("No such element")

    def get_clickable_element_from_use_case(self, use_case):
        return use_case.find_element_by_tag_name("a")