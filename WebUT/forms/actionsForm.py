from WebUT.forms.folderForm import FolderForm
from WebUT.forms.methodForm import MethodForm
from WebUT.forms.organizationForm import OrganizationForm
from WebUT.forms.standardForm import StandardForm
from WebUT.forms.toolForm import ToolForm
from WebUT.forms.useCaseForm import UseCaseForm
from .form import *

class ActionsForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.deleteButton = "//li[@id='plone-contentmenu-actions']/ul/li/a[contains(text(), 'Delete')]"
        self.deleteSubmit = "//input[@id='form-buttons-Delete']"

    def delete(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.deleteButton))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.deleteSubmit))
