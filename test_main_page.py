from main_page import PageOne
from utils import check_text_equal, check_text_contains


# Test run
class TestClass:

    def test_positive(self, driver):
        name = "Some Name"
        email = "test@test.com"
        page_one = PageOne(driver)
        page_one.open_page()
        page_one.user_name.input_text(name)
        page_one.user_email.input_text(email)
        page_one.submit_button.scroll_to_element()
        page_one.submit_button.click_element()
        check_text_equal(page_one.name.get_text(), f"Name:{name}")
        check_text_equal(page_one.email.get_text(), f"Email:{email}")

    def test_negative(self, driver):
        email = "test@test.test"
        page_one = PageOne(driver)
        page_one.open_page()
        page_one.user_email.input_text(email)
        page_one.submit_button.scroll_to_element()
        page_one.submit_button.click_element()
        check_text_contains(page_one.user_email.get_attribute("class"), "field-error")
