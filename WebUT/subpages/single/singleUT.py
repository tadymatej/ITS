import sys
sys.path.append("..")

from selenium import webdriver
from ..subpage import *

class SingleUT(SubPageUT):
    def __init__(self, driver : webdriver.Firefox, url):
        super().__init__(driver, url)