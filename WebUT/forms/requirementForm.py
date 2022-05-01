from .form import *





class RequirementForm(FormUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.submitElement = "//input[@id='form-buttons-save']"
        self.titleInput = "//input[@id='form-widgets-IDublinCore-title']"
        self.summaryInput = "//textarea[@id='form-widgets-IDublinCore-description']"

        self.idInput = "//input[@id='form-widgets-requirement_id']"
        self.textualDescriptionInput = "//textarea[@id='form-widgets-requirement_textual_description']"
        self.requirementTypeInput = "//select[@id='form-widgets-requirement_type']"

    def fill_in(self, title, summary = "", id = "", textualDescription = "", type = "S"):
        self.driver.find_element_by_xpath(self.titleInput).send_keys(title)
        self.driver.find_element_by_xpath(self.summaryInput).send_keys(summary)

        self.driver.find_element_by_xpath(self.idInput).send_keys(id)
        self.driver.find_element_by_xpath(self.textualDescriptionInput).send_keys(textualDescription)
        self.driver.find_element_by_xpath(self.requirementTypeInput).send_keys(type)

