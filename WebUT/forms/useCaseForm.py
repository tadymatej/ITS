from curses import KEY_BACKSPACE, KEY_ENTER
from .form import *
from WebUT.forms.inputs.relationsInput import RelationsInput

class UseCaseForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IBasic-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IBasic-description']"
        self.useCaseNumberInput = "//select[@id='form-widgets-use_case_number']"
        self.useCaseDomainInput = "//select[@id='form-widgets-use_case_domain']"
        self.useCaseProviderInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-use_case_provider']/div/div/ul/li/input")
        self.partnersInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-partners']/div/div/ul/li/input")
        self.useCaseDescriptionInput = "//iframe"
        self.useCaseEvaluationScenariosOptionElement = "//form/nav/a[contains(text(), 'Use case Evaluatuion Scenarios')]"
        self.defaultOptionElement = "//form/nav/a[contains(text(), 'Default')]"
        self.evaluationScenariosListInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-evaluation_scenario']/div/div/ul/li/input")
    
    def fill_in(self, title, summary="", useCaseNumber="", useCaseDomain="", useCaseProvider="", partners=[], description="", evaluationScenarios=[]):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.defaultOptionElement))
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
        self.driver.find_element_by_xpath(self.useCaseNumberInput).send_keys(useCaseNumber)
        self.driver.find_element_by_xpath(self.useCaseNumberInput).send_keys(KEY_ENTER)
        self.driver.find_element_by_xpath(self.useCaseDomainInput).send_keys(useCaseDomain)

        self.driver.find_element_by_xpath(self.useCaseDomainInput).send_keys(KEY_ENTER)
        
        if(useCaseProvider != ""):
            self.useCaseProviderInput.path_from_home()
            self.useCaseProviderInput.add_relation(useCaseProvider)
        
        if(len(partners) > 0):
            self.partnersInput.path_from_home()
            self.partnersInput.add_relations(partners)

        el = self.driver.find_element_by_xpath(self.useCaseDescriptionInput)
        el.click()
        el.send_keys(description)

        if(len(evaluationScenarios) > 0):
            self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.useCaseEvaluationScenariosOptionElement))
            self.evaluationScenariosListInput.path_from_home()
            self.evaluationScenariosListInput.add_relations(evaluationScenarios)