


from time import sleep
from .subpage import *


class ToolsPageUT(SubPageUT):
    def __init__(self, driver, url):
        SubPageUT.__init__(self, driver, url)
        self.toolsListElements = "//div[@id='faceted-results']/div/article"
        self.toolsListLoggedInElements = "//div[@id='faceted-results']/div/table/tbody/tr"
        self.letterFilterXpathStart = "//span[@class='faceted_letter'"
    
    def filter_by_first_character(self, char):
        el = self.driver.find_element_by_xpath(self.letterFilterXpathStart + " and contains(text(), '" + char.upper() + "')]")
        self.driver.execute_script("arguments[0].click()", el)
        sleep(1)

    def get_tools_list(self):
        tools = self.driver.find_elements_by_xpath(self.toolsListElements)
        if(len(tools) == 0):
            return self.driver.find_elements_by_xpath(self.toolsListLoggedInElements)
        else:
            return tools

    def find_tool_by_name(self, name):
        tools = self.get_tools_list()
        for tool in tools:
            try:
                tool.find_element_by_link_text(name)
                return tool
            except(Exception):
                pass
        
        raise Exception("No such element")

    def get_clickable_element_from_tool(self, tool):
        return tool.find_element_by_tag_name("a")