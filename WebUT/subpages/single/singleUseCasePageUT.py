from .singleUT import *

class SingleUseCasePageUT(SingleUT):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.titleElement = "//article[@id='content']/header/h1"
        self.summaryElement = "//article[@id='content']/header/div[@class='documentDescription description']"
        self.useCaseNumberElement = "//span[@id='form-widgets-use_case_number']/span"
        self.useCaseDomainElement = "//span[@id='form-widgets-use_case_domain']/span"
        self.useCaseProviderElement = "//span[@id='form-widgets-use_case_provider']/div/ul/li/span/a/span[1]"
        self.partnersElements = "//span[@id='form-widgets-partners']/div/ul/li"
        self.descriptionElement = "//div[@id='formfield-form-widgets-use_case_description']/p"
        self.evaluationScenariosElements = "//span[@id='form-widgets-evaluation_scenario']/div/ul/li"

    def get_title_content(self):
        return self.driver.find_element_by_xpath(self.titleElement).get_attribute("innerText")

    def get_summary_content(self):
        return self.driver.find_element_by_xpath(self.summaryElement).get_attribute("innerText")

    def get_use_case_number_content(self):
        return self.driver.find_element_by_xpath(self.useCaseNumberElement).get_attribute("innerText")

    def get_use_case_domain_content(self):
        return self.driver.find_element_by_xpath(self.useCaseDomainElement).get_attribute("innerText")

    def get_use_case_provider_content(self):
        return self.driver.find_element_by_xpath(self.useCaseProviderElement).get_attribute("innerText")

    def get_description_content(self):
        return self.driver.find_element_by_xpath(self.descriptionElement).get_attribute("innerText")


    def get_partners(self):
        return self.driver.find_elements_by_xpath(self.partnersElements)

    def get_evaluation_scenarios(self):
        return self.driver.find_elements_by_xpath(self.evaluationScenariosElements)
    