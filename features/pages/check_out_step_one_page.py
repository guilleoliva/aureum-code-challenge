import time

from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class CheckOutStepOne(BasePage):
    checkout = (By.XPATH, "//*[@data-test='checkout']")
    first_name = (By.XPATH, "//*[@data-test='firstName']")
    last_name = (By.XPATH, "//*[@data-test='lastName']")
    postal_code = (By.XPATH, "//*[@data-test='postalCode']")
    continue_btn = (By.XPATH, "//*[@data-test='continue']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def fill_first_name(self, name):
        try:
            user_name = self.web_utils.find_element(*self.first_name)
            user_name.click()
            user_name.send_keys(name)
        except Exception:
            raise Exception("Something went wrong, can not fill the first name information")

    def fill_last_name(self, last_name):
        try:
            user_name = self.web_utils.find_element(*self.last_name)
            user_name.click()
            user_name.send_keys(last_name)
        except Exception:
            raise Exception("Something went wrong, can not fill the last name information")

    def fill_postal_code(self, postal_code):
        try:
            user_name = self.web_utils.find_element(*self.postal_code)
            user_name.click()
            user_name.send_keys(postal_code)
        except Exception:
            raise Exception("Something went wrong, can not fill the postal code information")

    def click_on_continue(self):
        try:
            self.web_utils.find_element(*self.continue_btn).click()
        except Exception:
            raise Exception("Something went wrong, can not click on the continue button")

    def fill_user_information(self, name, last_name, postal_code):
        self.fill_first_name(name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
