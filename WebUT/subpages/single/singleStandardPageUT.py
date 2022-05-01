from .singleUT import *

class SingleStandardPageUT(SingleUT):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.titleElement = "//article[@id='content']/header/h1"
        self.summaryElement = "//article[@id='content']/header/div[@class='documentDescription description']"

    def get_title_content(self):
        return self.driver.find_element_by_xpath(self.titleElement).get_attribute("innerText")
    
    def get_summary_content(self):
        return self.driver.find_element_by_xpath(self.summaryElement).get_attribute("innerText")