from .singleUT import *

class SingleOrganizationPageUT(SingleUT):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.titleElement = "//article[@id='content']/header/h1"
        self.summaryElement = "//article[@id='content']/header/div[@class='documentDescription description']"
        self.acronymElement = "//span[@id='form-widgets-organization_acronym']"
        self.urlElement = "//span[@id='form-widgets-organization_url']/a"
        self.descriptionElement = "//div[@id='formfield-form-widgets-organization_description']/p"
        self.contactElement = "//span[@id='form-widgets-organization_contact_person']"
        self.contactEmailElement = "//span[@id='form-widgets-organization_contact_email']/a"

    def get_title_content(self):
        return self.driver.find_element_by_xpath(self.titleElement).get_attribute("innerText")

    def get_summary_content(self):
        return self.driver.find_element_by_xpath(self.summaryElement).get_attribute("innerText")

    def get_acronym_content(self):
        return self.driver.find_element_by_xpath(self.acronymElement).get_attribute("innerText")

    def get_url_content(self):
        return self.driver.find_element_by_xpath(self.urlElement).get_attribute("innerText")

    def get_description_content(self):
        return self.driver.find_element_by_xpath(self.descriptionElement).get_attribute("innerText")

    def get_contact_content(self):
        return self.driver.find_element_by_xpath(self.contactElement).get_attribute("innerText")

    def get_contact_email_content(self):
        return self.driver.find_element_by_xpath(self.contactEmailElement).get_attribute("innerText")