class FoundationPage():

    def __init__(self, driver):
        self._driver = driver

    def open_page(self):
        if hasattr(self, 'link'):
            self._driver.get(self.link)
        else:
            raise AssertionError('Class does not have attribute \'link\'')