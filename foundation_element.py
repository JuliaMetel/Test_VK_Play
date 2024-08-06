from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FoundationElement():
    def __init__(self, locator, driver, wait_presence=False):
        if wait_presence:
            wait = WebDriverWait(driver, 2, poll_frequency=0.1)
            wait.until(
                method=expected_conditions.presence_of_element_located(locator),
                message=f"Error of waiting the element with selector: {locator}."
            )
        self.__element = driver.find_element(*locator)
        self.driver = driver

    def click_element(self):
        self.__element.click()

    def input_text(self, text):
        self.__element.send_keys(*text)

    def get_text(self):
        return self.__element.text

    def scroll_to_element(self) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.__element)

    def get_attribute(self, name):
        return self.__element.get_attribute(name)



