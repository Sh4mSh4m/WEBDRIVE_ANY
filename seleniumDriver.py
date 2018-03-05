import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os


class PiloteSel(webdriver.Chrome):


    def __init__(self, headless=True):
        """
        Inherits from Selenium webdriver.Chrome class
        Constructor initiated with headless options 
        Instance is initiated with super method implicitly_wait
        which means driver will timeout after X seconds polling 
        presence of the item every 500ms.
        """
        if headless:
            pilote_options = Options()
            pilote_options.add_argument('--headless --window-size=1920,1080')
            pilote_options.add_argument('--disable-gpu')
            pilote_options.add_argument('log-level=3')
        super().__init__(options=pilote_options)
        super().implicitly_wait(5)

    def selectElt(self, xpath):
        """
        Verifies xpath is valid
        Returns DOM element on which the driver is set on
        for further action. Search is based on xpath
        """
        targetElt = super().find_element_by_xpath(xpath)
        return targetElt

    def clickOn(self, selectElt):
        """
        Performs webdriver click method on selected element.
        Does not return anything
        """
        selectElt.super().click()
        

    def getUrl(self, url):
        """
        Vérifies input is a proper url
        Gets the driver to browse to that URL
        """
        super().get(url)

    def getScreenshot(self, fileName):
        """
        Takes a screenshot of current page browsed by driver
        Takes filename as input and outputs a PNG file in current folder
        If you specify path, it must exist
        """
        super().get_screenshot_as_file('{}.png'.format(fileName))


# plt_dd/mm/yyyy_X
#take a snapshot

if __name__ == '__main__':
    pilote = PiloteSel()
    pilote.getUrl('https://www.google.com')
    pilote.getScreenshot('bobby')
    print('done')
