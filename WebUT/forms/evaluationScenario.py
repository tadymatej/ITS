from time import sleep
from .form import *
from WebUT.forms.inputs.relationsInput import RelationsInput

class EvaluationScenarioForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IDublinCore-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IDublinCore-description']"

        self.idInput = "//textarea[@id='form-widgets-evaluation_secnario_id']"
        self.textualDescriptionInput = "//input[@id='form-widgets-evaluation_scenario_textual_description']"
        self.riskInput = "//input[@id='form-widgets-evaluation_scenario_rationale_risk']"

    def fill_in(self, title, summary = "", id = "", textualDescription = "", risk = ""):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
        self.driver.find_element_by_xpath(self.idInput).send_keys(id)
        self.driver.find_element_by_xpath(self.textualDescriptionInput).send_keys(textualDescription)
        self.driver.find_element_by_xpath(self.riskInput).send_keys(risk)

