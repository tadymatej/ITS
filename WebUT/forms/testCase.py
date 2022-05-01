from time import sleep
from .form import *
from WebUT.forms.inputs.relationsInput import RelationsInput

class TestCaseForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IDublinCore-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IDublinCore-description']"
        self.testCaseIdInput = "//input[@id='form-widgets-test_case_id']"
        self.caseEvalCriteriaInput = "//select[@id='form-widgets-test_case_evaluation_criteria']"
        self.VVmethod = RelationsInput(driver, "//div[@id='formfield-form-widgets-test_case_v_v_method']/div/div/ul/li/input")
        self.componentUnderEvaluationInput = "//input[@id='form-widgets-test_case_evaluation_criteria']"


    def fill_in(self, title, summary = "", id = "", evalCriteria = "F", VVmethod = "", componentUnderEvaluation = ""):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
        self.driver.find_element_by_xpath(self.testCaseIdInput).send_keys(id)
        
        evalCriteriaSelect = self.driver.find_element_by_xpath(self.caseEvalCriteriaInput)
        evalCriteriaSelect.send_keys(evalCriteria)

        if(VVmethod != ""):
            self.VVmethod.path_from_home()
            self.VVmethod.add_relation(VVmethod)

        self.driver.find_element_by_xpath(self.componentUnderEvaluationInput).send_keys(componentUnderEvaluation)
        