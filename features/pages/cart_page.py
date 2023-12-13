import time

from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class CartPage(BasePage):
    checkout = (By.XPATH, "//*[@data-test='checkout']")
    inventory_item_name = (By.XPATH, "//div[@class='inventory_item_name' and text()='{}']")
    item_price = (By.XPATH, "./parent::a/following-sibling::div/descendant::div[@class='inventory_item_price']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def click_on_checkout(self):
        try:
            self.web_utils.find_element(*self.checkout).click()
        except Exception:
            raise Exception('Something went wrong, can not get the checkout button')

    def is_item_and_price_in_cart(self, item, price):
        try:
            title = self.web_utils.find_element(self.inventory_item_name[0], self.inventory_item_name[1].format(item))
            item_price = title.find_element(*self.item_price).text[1::]
            return True if price == item_price else False
        except Exception:
            raise Exception('Something went wrong, can not get the item price')
