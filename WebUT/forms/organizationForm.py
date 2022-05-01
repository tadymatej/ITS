from .form import *

class OrganizationForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IBasic-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IBasic-description']"
        self.acronymInput = "//input[@id='form-widgets-organization_acronym']"
        self.urlInput = "//input[@id='form-widgets-organization_url']"
        self.contactPersonInput = "//input[@id='form-widgets-organization_contact_person']"
        self.contactEmailInput = "//input[@id='form-widgets-organization_contact_email']"
        self.descriptionInput = "//iframe"

    def fill_in(self, title, summary="", acronym="", url="", contactPerson="", contactEmail="", description=""):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
        self.driver.find_element_by_xpath(self.acronymInput).send_keys(acronym)
        self.driver.find_element_by_xpath(self.urlInput).send_keys(url)
        self.driver.find_element_by_xpath(self.contactPersonInput).send_keys(contactPerson)
        self.driver.find_element_by_xpath(self.contactEmailInput).send_keys(contactEmail)
        self.driver.find_element_by_xpath(self.descriptionInput).send_keys(description)
