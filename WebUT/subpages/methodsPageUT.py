from time import sleep
from .subpage import *

class MethodsPageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.methodsListElements = "//div[@id='faceted-results']/div/article"
        self.methodsListLoggedInElements = "//div[@id='faceted-results']/div/table/tbody/tr"
        self.letterFilterXpathStart = "//span[@class='faceted_letter'"

    def filter_by_first_character(self, char : str):
        el = self.driver.find_element_by_xpath(self.letterFilterXpathStart + " and contains(text(), '" + char.upper() + "')]")
        self.driver.execute_script("arguments[0].click()", el)
        sleep(1)

    def get_methods_list(self):
        methods = self.driver.find_elements_by_xpath(self.methodsListElements)
        if(len(methods) == 0):
            return self.driver.find_elements_by_xpath(self.methodsListLoggedInElements)
        else:
            return methods

    def find_method_by_name(self, name):
        methods = self.get_methods_list()
        for method in methods:
            try:
                method.find_element_by_link_text(name)
                return method
            except(Exception):
                pass
        
        raise Exception("No such element")

    def get_clickable_element_from_method(self, method):
        return method.find_element_by_tag_name("a")