import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class CheckOutComplete(BasePage):
    thank_you = (By.XPATH, "//h2[text()='Thank you for your order!']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def is_thank_you_message_present(self):
        try:
            return True if self.web_utils.find_element(*self.thank_you).is_displayed() else False
        except Exception:
            raise Exception("Something went wrong, can not get the thank you message")
