from curses import KEY_ENTER
from selenium import webdriver

from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class FormUT:
    def __init__(self, driver : webdriver.Firefox):
        self.submitElement = ""
        self.driver = driver

    def submit(self):
        #el = ui.WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.submitElement)))
        el = self.driver.find_element_by_xpath(self.submitElement)
        self.driver.execute_script("arguments[0].click();", el)