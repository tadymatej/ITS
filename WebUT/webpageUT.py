from selenium import webdriver


class WebPageUT:
    
    def __init__(self, driver : webdriver.Firefox):
        self.driver = driver
        self.loggedIn = False
        self.loggedInAs = ""
        self.actualPage = None
