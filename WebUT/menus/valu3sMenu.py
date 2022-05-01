
from .menu import *

class Valu3sMenu(MenuUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.methodsButton = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'Methods')]"
        self.toolsButton = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'Tools')]"
        self.aboutButton = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'About')]"
        self.useCasesButton = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'Use Cases')]"
        self.organizations = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'Organizations')]"
        self.value3sGlossary = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'VALU3S Glossary')]"
        self.standards = "//ul[@id='portal-globalnav']/li/a[contains(text(), 'Standards')]"
    
    def navigate_to_methods(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.methodsButton))

    def navigate_to_tools(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.toolsButton))

    def navigate_to_aboutPage(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.aboutButton))

    def navigate_to_useCases(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.useCasesButton))

    def navigate_to_organizations(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.organizations))

    def navigate_to_glossary(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.value3sGlossary))

    def navigate_to_standards(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.standards))
