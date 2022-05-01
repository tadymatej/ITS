from .singleUT import *

class SingleToolPageUT(SingleUT):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.titleElement = "//article[@id='content']/header/h1"
        self.summaryElement = "//article[@id='content']/header/div[@class='documentDescription description']"
        self.purposeElement = "//span[@id='form-widgets-tool_purpose']"
        self.descriptionElement = "//div[@id='formfield-form-widgets-tool_description']/p"
        self.strengthsElement = "//div[@id='formfield-form-widgets-tool_strengths']"
        self.toolLimitationsElement = "//div[@id='formfield-form-widgets-tool_limitations']"
        self.toolReferencesElement = "//div[@id='formfield-form-widgets-tool_references']"
        self.relatedMethodsElements = "//span[@id='form-widgets-related_methods']/div/ul/li"
        self.testCaseOrVVActivityElement = "//span[@id='form-widgets-test_case_or_verification_and_validation_activity']/div/ul/li"
        self.standardElements = "//span[@id='form-widgets-standards']/div/ul/li"

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
        return self.driver.find_element_by_xpath(self.toolLimitationsElement).get_attribute("innerText")

    def get_references_content(self):
        return self.driver.find_element_by_xpath(self.toolReferencesElement).get_attribute("innerText")

    def get_test_case_or_vv_activity(self):
        return self.driver.find_element_by_xpath(self.testCaseOrVVActivityElement).get_attribute("innerText")


    def get_standards(self):
        return self.driver.find_elements_by_xpath(self.standardElements)

    def get_related_methods(self):
        return self.driver.find_elements_by_xpath(self.relatedMethodsElements)