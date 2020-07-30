from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(DuckDuckGoSearchPage.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*DuckDuckGoSearchPage.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)