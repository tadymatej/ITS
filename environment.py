
from selenium import webdriver

from valu3sUT import *

class TestingPage:
    """
    Třída obsahující informace o driveru testované stránky, stará se o otevření webu, přihlášení se na web...
    """
    def getDriverWebPage(self):
        """
        Vrátí otevřený driver stránky
        """
        return self.driverWebPage

    def __init__(self, url, needsLogin, browser , driverExecutablePath):
        """
        Inicializuje stránku, neotevře
        Arguments
        ---------
        url - adresa stránky, která se má otevřít
        needsLogin - bool, označující, zda se musí přihlásit na web
        browser - Typ prohlížeče z množiny: {"Firefox", "Chrome"}
        driverExecutablePath - Cesta k otevření driveru
        """
        self.url = url
        self.needsLogin = needsLogin
        self.loggedIn = False
        if(browser == "Firefox"): self.driverWebPage= webdriver.Firefox(executable_path=driverExecutablePath)
        elif(browser == "Chrome"): self.driverWebPage= webdriver.Chrome(executable_path=driverExecutablePath)
        self.driverWebPage.implicitly_wait(15)
    
    def logIn(self, loggingPage, email, password, submitValueButton): #type: (TestingPage, str, str, str, WebElement) -> None
        """
        Přihlášení se na web
        Arguments
        ---------
        loggingPage - stránka, na které je přihlašovací formulář (url)
        email - email, na který se má přihlásit
        password - heslo k emailu
        submitValueButton - WebElement určující, které tlačítko submituje formulář
        """
        self.loggedIn=True
        self.driverWebPage.get(loggingPage)
        emailField = self.driverWebPage.find_element(by=By.ID, value="email-login") #type: WebElement
        emailField.send_keys(email)
        passwordField = self.driverWebPage.find_element(by=By.ID, value="heslo-login") #type: WebElement
        passwordField.send_keys(password)
        submitField = self.driverWebPage.find_element(by=By.XPATH, value=submitValueButton)  #type: WebElement
        submitField.click()

    def openPage(self, *args):
        """
        Otevře webovou stránku, v případě potřeby provede i přihlášení
        Arguments
        ---------
        args = email, heslo, textButtonuSubmit
        """
        if(self.needsLogin): 
            if(len(args) < 4): return 
            self.logIn(args[0], args[1], args[2], args[3])
        self.driverWebPage.get(self.url)

    def closePage(self):
        """
        Ukončí a uzavře otevřenou stránku
        """
        self.driverWebPage.close()

#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

def get_driver():
    '''Get Firefox/Chrome driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    driver.implicitly_wait(15)

    # Web stranku ziskate nasledujicim:
    # (jedno nebo druhe, zalezi na nastaveni prostedi)
    # driver.get("http://valu3s:8080/repo")
    # driver.get("http://localhost:8080/repo")

    return driver

    # Nezapomente vzdy po ukonceni testovani zavrit driver:
    # driver.close()


#TODO: předělat na get_driver() !!!
def before_feature(context, feature):
    testingPage = TestingPage("http://localhost:8080/repo", False, "Firefox", "/home/matej/bin/geckodriver")
    context.valu3sWeb = Valu3sUT(testingPage.getDriverWebPage())
    context.GLOBALS = dict()
    context.datas = dict()
    context.types = dict()

def after_feature(context, feature):
    context.testingPage.closePage()