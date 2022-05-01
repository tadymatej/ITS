from time import sleep
from .subpage import *

class OrganizationsPageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.organizationsListElements = "//div[@id='faceted-results']/div/article"
        self.organizationsListLoggedInElements = "//div[@id='faceted-results']/div/table/tbody/tr"
        self.letterFilterXpathStart = "//span[@class='faceted_letter'"

    def filter_by_first_character(self, char):
        el = self.driver.find_element_by_xpath(self.letterFilterXpathStart + " and contains(text(), '" + char.upper() + "')]")
        self.driver.execute_script("arguments[0].click()", el)
        sleep(1)

    def get_organizations_list(self):
        organizations = self.driver.find_elements_by_xpath(self.organizationsListElements)
        if(len(organizations) == 0):
            return self.driver.find_elements_by_xpath(self.organizationsListLoggedInElements)
        else:
            return organizations

    def find_organization_by_name(self, name):
        organizations = self.get_organizations_list()
        for organization in organizations:
            try:
                organization.find_element_by_link_text(name)
                return organization
            except(Exception):
                pass
        
        raise Exception("No such element")

    def get_clickable_element_from_organization(self, organization):
        return organization.find_element_by_tag_name("a")