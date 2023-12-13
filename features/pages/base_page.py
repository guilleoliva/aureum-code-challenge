import time

from selenium.webdriver.common.by import By

from .web_utils import WebUtils


class BasePage:
    page_loading_time = 0
    xpath_lower_text = "translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
    xpath_lower_string = "translate(string(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
    button = (By.XPATH, "//button[contains(text(),'{}')]")
    burger_menu = (By.ID, 'react-burger-menu-btn')
    log_out = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        self.start_time = time.time()
        self.driver = driver
        self.web_utils = WebUtils(driver)

    def get_page_loading_time(self):
        return self.page_loading_time

    def get_current_url(self):
        return self.driver.current_url

    def go_to_previous_page(self):
        return self.driver.back()
