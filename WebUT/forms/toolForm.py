from time import sleep
from .form import *
from WebUT.forms.inputs.relationsInput import RelationsInput

class ToolForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IDublinCore-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IDublinCore-description']"
        self.purposeInput = "//textarea[@id='form-widgets-tool_purpose']"
        self.descriptionInput = "//iframe[1]"
        self.strengthsInput = "//iframe[2]"
        self.limitationsInput = "//iframe[3]"
        self.referencesInput = "//iframe[4]"
        self.defaultOptionElement = "//form/nav/a[contains(text(), 'Default')]"
        self.relationsOptionElement = "//form/nav/a[contains(text(), 'Relations')]"

        self.relatedMethodsInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-related_methods']/div/div/ul/li/input")
        self.testCaseOrVVActivityInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-test_case_or_verification_and_validation_activity']/div/div/ul/li/input")
        self.standardsInput = RelationsInput(driver, "//div[@id='formfield-form-widgets-standards']/div/div/ul/li/input")

    def fill_in(self, title, summary = "", purpose = "", description = "", strengths = "", limitations = "", references = "", relatedMethods = [], testCaseOrVVActivity = "", standards = []):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)
        self.driver.find_element_by_xpath(self.purposeInput).send_keys(purpose)
        iframes = self.driver.find_elements_by_tag_name("iframe")
        desc_input = iframes[0]
        desc_input.click()
        desc_input.send_keys(description)
        strengths_input = iframes[1]
        strengths_input.click()
        strengths_input.send_keys(strengths)
        limitations_input = iframes[2]
        limitations_input.click()
        limitations_input.send_keys(limitations)
        references_input = iframes[3]
        references_input.click()
        references_input.send_keys(references)

        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.relationsOptionElement))
        sleep(1)

        if(len(relatedMethods) > 0):
            self.relatedMethodsInput.path_from_home()
            self.relatedMethodsInput.add_relations(relatedMethods)

        if(testCaseOrVVActivity != ""):
            self.testCaseOrVVActivityInput.path_from_home()
            self.testCaseOrVVActivityInput.add_relation(testCaseOrVVActivity)

        if(len(standards) > 0):
            self.standardsInput.path_from_home()
            self.standardsInput.add_relations(standards)
