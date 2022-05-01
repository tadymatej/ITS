from time import sleep
from .subpage import *

class StandardsPageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.standardsListElements = "//article[@class='entry']"
        self.letterFilterXpathStart = "//span[@class='faceted_letter'"

    def filter_by_first_character(self, char):
        el = self.driver.find_element_by_xpath(self.letterFilterXpathStart + " and contains(text(), '" + char.upper() + "')]")
        self.driver.execute_script("arguments[0].click()", el)
        sleep(1)
    
    def get_standards_list(self):
        standards = self.driver.find_elements_by_xpath(self.standardsListElements)
        if(len(standards) == 0):
            return self.driver.find_elements_by_xpath(self.standardsListLoggedInElements)
        else:
            return standards

    def find_standard_by_name(self, name):
        standards = self.get_standards_list()
        for standard in standards:
            try:
                standard.find_element_by_link_text(name)
                return standard
            except(Exception):
                pass
        
        raise Exception("No such element")

    def get_clickable_element_from_standard(self, standard):
        return standard.find_element_by_tag_name("a")