import time

from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class CheckOutStepTwo(BasePage):
    finish = (By.XPATH, "//*[@data-test='finish']")
    summary_info_label = (By.CLASS_NAME, "summary_info_label")
    summary_value_label = (By.CLASS_NAME, "summary_value_label")
    summary_subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
    summary_tax_label = (By.CLASS_NAME, "summary_tax_label")
    summary_total_label = (By.CLASS_NAME, "summary_total_label")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def is_payment_information_present(self):
        try:
            summary_info = self.web_utils.find_element(*self.summary_info_label)
            summary_value_label = self.web_utils.find_element(*self.summary_value_label)
            summary_subtotal_label = self.web_utils.find_element(*self.summary_subtotal_label)
            summary_tax_label = self.web_utils.find_element(*self.summary_tax_label)
            return (
                True
                if summary_info.is_displayed()
                and summary_value_label.is_displayed()
                and summary_tax_label.is_displayed()
                and summary_subtotal_label.is_displayed()
                else False
            )
        except Exception:
            raise Exception("Something went wrong, can not get the checkout payment information")

    def click_on_finish(self):
        try:
            self.web_utils.find_element(*self.finish).click()
        except Exception:
            raise Exception("Something went wrong, can not get the finish button")

    def get_sub_total_price(self):
        try:
            subtotal = self.web_utils.find_element(*self.summary_subtotal_label).text
            return subtotal.split('$')[1]
        except Exception:
            raise Exception("Something went wrong, can not get the subtotal information")
