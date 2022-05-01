from .singleUT import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SingleMethodPageUT(SingleUT):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.titleElement = "//article[@id='content']/header/h1"
        self.summaryElement = "//article[@id='content']/header/div[@class='documentDescription description']"
        self.purposeElement = "//span[@id='form-widgets-method_purpose']"
        self.descriptionElement = "//div[@id='formfield-form-widgets-method_description']/p"
        self.strengthsElement = "//div[@id='formfield-form-widgets-method_strengths']"
        self.limitationsElement = "//div[@id='formfield-form-widgets-method_limitations']"
        self.referencesElement = "//div[@id='formfield-form-widgets-method_references']"
        self.relatedMethodsElements = "//span[@id='form-widgets-related_methods']/div/ul/li"
        self.toolsElements = "//span[@id='form-widgets-tools']/div/ul/li"
        self.partMethodElement = "//div[@id='formfield-form-widgets-part_method']" #TODO budu muset hledat někde více uvnitř
        self.testCaseOrVVActivityElement = "//span[@id='form-widgets-test_case_or_verification_and_validation_activity']/div/ul/li"
        self.standardsElements = "//span[@id='form-widgets-standards']/div/ul/li"

    def get_title_content(self):
        return self.driver.find_element_by_xpath(self.titleElement).get_attribute("innerText")

    def get_summary_content(self):
        return self.driver.find_element_by_xpath(self.summaryElement).get_attribute("innerText")

    def get_purpose_content(self):
        return self.driver.find_element_by_xpath(self.purposeElement).get_attribute("innerText")

    def get_description_content(self):
        return self.driver.find_element_by_xpath(self.descriptionElement).get_attribute("innerText")

    def get_strengths_content(self):
        return self.driver.find_element_by_xpath(self.strengthsElement).get_attribute("innerText")

    def get_limitations_content(self):
        return self.driver.find_element_by_xpath(self.limitationsElement).get_attribute("innerText")

    def get_references_content(self):
        return self.driver.find_element_by_xpath(self.referencesElement).get_attribute("innerText")

    def get_part_method_content(self):
        return self.driver.find_element_by_xpath(self.partMethodElement).get_attribute("innerText")

    def get_test_case_or_vv_activity_content(self):
        return self.driver.find_element_by_xpath(self.testCaseOrVVActivityElement).get_attribute("innerText")
    

    def get_related_methods(self):
        return self.driver.find_elements_by_xpath(self.relatedMethodsElements)

    def get_tools(self):
        return self.driver.find_elements_by_xpath(self.toolsElements)

    def get_standards(self):
        return self.driver.find_elements_by_xpath(self.standardsElements)