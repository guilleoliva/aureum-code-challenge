import time

from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LandingPage(BasePage):
    logo_icon = (By.CLASS_NAME, "login_logo")
    user_name = (By.XPATH, "//*[@data-test='username']")
    user_password = (By.XPATH, "//*[@data-test='password']")
    log_in_btn = (By.XPATH, "//*[@data-test='login-button']")
    log_in_error = (By.XPATH, "//*[@data-test='error']")
    form = (By.XPATH, "//form")

    def __init__(self, driver, app_url):
        super().__init__(driver)
        self.login_url = app_url
        self.page_loading_time = time.time() - self.start_time

    def open_app(self):
        self.web_utils.get(self.login_url)

    def logs_in(self, user, password):
        self.fill_user_name(user)
        self.fill_password(password)

    def fill_user_name(self, user):
        try:
            user_name = self.web_utils.find_element(*self.user_name)
            user_name.click()
            user_name.send_keys(user)
        except Exception:
            raise Exception("Something went wrong, can not fill the username information")

    def fill_password(self, password):
        try:
            user_password = self.web_utils.find_element(*self.user_password)
            user_password.click()
            user_password.send_keys(password)
        except Exception:
            raise Exception("Something went wrong, can not fill the password information")

    def submit_login(self):
        time.sleep(1)
        try:
            self.web_utils.find_element(*self.log_in_btn).click()
        except Exception:
            raise Exception("Something went wrong, can not find the submit button")

    def is_swags_icon_present(self):
        try:
            return True if self.driver.find_element(*self.logo_icon).is_displayed() else False
        except Exception:
            raise Exception("Something went wrong, can not find the logo icon")

    def login_error_message(self, message):
        try:
            return True if self.driver.find_element(*self.log_in_error).text == 'Epic sadface: ' + message else False
        except Exception:
            raise Exception(f'Expected message "{message}" not present')
