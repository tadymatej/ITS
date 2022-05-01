from selenium import webdriver

class SubPageUT:
    def __init__(self, driver : webdriver.Firefox, url):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)