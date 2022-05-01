from curses import *
from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver

from .input import *

class RelationsInput(Input):
    def __init__(self, driver, input_xpath):
        super().__init__(driver)
        self.input = input_xpath

    def get_results_list(self):
        el = self.driver.find_element_by_xpath(self.input)

    def get_path_elements(self):
        el = self.driver.find_element_by_xpath(self.input)
        path_wrapper = el.find_element_by_xpath("../../../../div/div[@class='path-wrapper']")
        pathElements = []
        pathElements.append(path_wrapper.find_element_by_xpath(".//a[@class='crumb']"))
        for el in path_wrapper.find_elements_by_xpath(".//span[@class='separator']"):
            pathElements.append(el)
        return pathElements
    
    def path_from_home(self):
        els = self.get_path_elements()
        self.driver.execute_script("arguments[0].click()", els[0])

    def add_relation(self, relation):
        input = self.driver.find_element_by_xpath(self.input)
        input.send_keys(relation)

        el = self.driver.find_element_by_xpath("//span[contains(@class, 'pattern-relateditems-result-title') and contains(text(), '" + relation + "')]")
        el.click()

    def add_relations(self, relations : list):
        for relation in relations:
            self.add_relation(relation)