from selenium.webdriver.common.by import By
from foundation_page import FoundationPage
from foundation_element import FoundationElement


class PageOne(FoundationPage):
    link = "https://demoqa.com/text-box"

    @property
    def submit_button(self):
        return FoundationElement((By.ID, 'submit'), self._driver)

    @property
    def user_name(self):
        return FoundationElement((By.ID, 'userName'), self._driver)

    @property
    def user_email(self):
        return FoundationElement((By.ID, 'userEmail'), self._driver)

    @property
    def name(self):
        return FoundationElement((By.ID, 'name'), self._driver, True)

    @property
    def email(self):
        return FoundationElement((By.ID, 'email'), self._driver, True)
