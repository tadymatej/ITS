
from pickle import TRUE
from time import sleep
from WebUT import *
from selenium import webdriver

class Valu3sUT(WebPageUT):
    def __init__(self, driver):
        super().__init__(driver)
        self.logInButton = "//div[@id='portal-anontools']/ul/li/a[contains(text(), 'Log in')]"
        self.homePage = HomePageUT(driver, "http://localhost:8080/repo")
        self.methodsPage = MethodsPageUT(driver, "http://localhost:8080/repo/method")
        self.toolsPage = ToolsPageUT(driver, "http://localhost:8080/repo/tools")
        self.useCasesPage = UseCasesPageUT(driver, "http://localhost:8080/repo/use-cases")
        self.organizationsPage = OrganizationsPageUT(driver, "http://localhost:8080/repo/organizations")
        self.standardsPage = StandardsPageUT(driver, "http://localhost:8080/repo/standards")
        self.menu = Valu3sMenu(driver)
        self.search = Valu3sSearch(driver)
        self.loggedInMenu = None #type: Valu3sAdministratorMenu
        self.loggedUserElement = "//li[@id='portal-personaltools']/a/span"

    def log_in(self, name, password):
        if self.loggedIn == False:
            self.homePage.logInForm.close()
            self.driver.execute_script("arguments[0].click()", self.driver.find_element_by_xpath(self.logInButton))
            self.homePage.logInForm.fill_in(name, password)



            self.homePage.logInForm.submit()
            try:
                self.driver.find_element_by_xpath(self.loggedUserElement + "[contains(text(), '" + name + "')]")
                self.loggedIn = True
                self.loggedInAs = name
                self.loggedInMenu = Valu3sAdministratorMenu(self.driver)
                return True
            except(Exception):
                return False

    def log_out(self):
        if(self.loggedIn == True):
            self.loggedInMenu.logout()
            self.loggedInAs = ""
            self.loggedIn = False
            self.loggedInMenu = None
