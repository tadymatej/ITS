import sys

from WebUT.forms.actionsForm import ActionsForm
sys.path.append("..")
from ..forms.addNewForm import *
from ..forms.actionsForm import *
from .menu import *

class Valu3sAdministratorMenu(MenuUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.logOutButton = "//div[@id='edit-zone']/div/nav/ul[@id='personal-bar-container']/li/a/span[@class='icon-user']"
        self.logOutButtonSubmit = "//li[@id='portal-personaltools']/ul/li/a[contains(text(), 'Log out')]"
        self.editButton = "//div[@id='edit-zone']/div/nav/ul[@class='plone-toolbar-main']/li/a/span[contains(text(), 'Edit')]"
        self.addNewButton = "//li[@id='plone-contentmenu-factories']/a/span[contains(text(), 'Add new')]"
        self.addNewForm = AddNewForm(driver)
        self.actionsButton = "//li[@id='plone-contentmenu-actions']/a/span[contains(text(), 'Actions')]"
        self.actionsForm = ActionsForm(driver)
        self.statePublishedPrivate = "//div[@id='edit-zone']/div/nav/ul[@class='plone-toolbar-main']/li/a/span/span[contains(text(), 'State:')]"
        self.statePublishElement = "//li[@id='plone-contentmenu-workflow']/ul/li/a[contains(text(), 'Publish')]"
        self.statePrivateElement = "//li[@id='plone-contentmenu-workflow']/ul/li/a[contains(text(), 'Send back')]"
    
    def edit(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.editButton))

    def addNew(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.addNewButton))

    def actions(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.actionsButton))

    def set_publish_state(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.statePublishedPrivate))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.statePublishElement))

    def set_private_state(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.statePublishedPrivate))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.statePrivateElement))

    def logout(self):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.logOutButton))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.logOutButtonSubmit))