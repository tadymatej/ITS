from unittest import TestCase
from WebUT.forms.evaluationScenario import EvaluationScenarioForm
from WebUT.forms.folderForm import FolderForm
from WebUT.forms.methodForm import MethodForm
from WebUT.forms.organizationForm import OrganizationForm
from WebUT.forms.standardForm import StandardForm
from WebUT.forms.testCase import TestCaseForm
from WebUT.forms.toolForm import ToolForm
from WebUT.forms.useCaseForm import UseCaseForm
from WebUT.forms.requirementForm import RequirementForm
from .form import *

class AddNewForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.evaluationScenarioButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Evaluation Scenario')]"
        self.folderButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Folder')]"
        self.methodButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Method')]"
        self.organizationButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Organization')]"
        self.requirementButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Requirement')]"
        self.standardButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Standard')]"
        self.testCaseButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Test Case')]"
        self.toolButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Tool')]"
        self.useCaseButton = "//li[@id='plone-contentmenu-factories']/ul/li/a[contains(text(), 'Use Case')]"
        self.submitElement = "//input[@id='buttons-login']"

        self.methodForm = MethodForm(driver)
        self.organizationForm = OrganizationForm(driver)
        self.folderForm = FolderForm(driver)
        self.standardForm = StandardForm(driver)
        self.toolForm = ToolForm(driver)
        self.useCaseForm = UseCaseForm(driver)
        self.evaluationScenarioForm = EvaluationScenarioForm(driver)
        self.testCaseForm = TestCaseForm(driver)
        self.requirementForm = RequirementForm(driver)

    
    def add_evaluation_scenario(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.evaluationScenarioButton))
        return self.evaluationScenarioForm
    
    def add_folder(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.folderButton))
        return self.folderForm
    
    def add_method(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.methodButton))
        return self.methodForm

    def add_organization(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.organizationButton))
        return self.organizationForm

    def add_requirement(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.requirementButton))
        return self.requirementForm

    def add_standard(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.standardButton))
        return self.standardForm

    def add_test_case(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.testCaseButton))
        return self.testCaseForm

    def add_tool(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.toolButton))
        return self.toolForm

    def add_use_case(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.useCaseButton))
        return self.useCaseForm