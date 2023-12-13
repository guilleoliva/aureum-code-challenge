import time

from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class InventoryPage(BasePage):
    inventory_item = (By.CLASS_NAME, 'inventory_item_name')
    item_price = (
        By.XPATH,
        ".//ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/descendant::div",
    )
    add_item = (
        By.XPATH,
        ".//ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/descendant::button",
    )
    shopping_cart_qty = (By.CLASS_NAME, "shopping_cart_badge")
    shopping_cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    sort_container = (By.XPATH, "//*[@data-test='product_sort_container']")
    high_to_low = (By.XPATH, "//option[@value='hilo']")
    z_to_a = (By.XPATH, "//option[@value='za']")
    inventory_list = (By.CLASS_NAME, "inventory_list")
    inventory_list_elements = (By.XPATH, './div')
    inventory_item_price = (By.CLASS_NAME, 'inventory_item_price')

    def __init__(self, driver):
        super().__init__(driver)
        self.page_loading_time = time.time() - self.start_time

    def add_item_to_cart(self, item_name):
        try:
            for item in self.web_utils.find_elements(*self.inventory_item):
                if item.text == item_name:
                    item.find_element(*self.add_item).click()
                    return item.find_element(*self.item_price).text[1::]
        except Exception:
            raise Exception(f'Something went wrong, can not find the item "{item_name}" inside the dashboard')

    def is_burger_menu_present(self):
        try:
            return True if self.web_utils.find_element(*self.burger_menu).is_displayed() else False
        except Exception:
            raise Exception('Something went wrong, can not find the burger menu')

    def get_cart_item_quantity(self):
        try:
            return self.web_utils.find_element(*self.shopping_cart_qty).text
        except Exception:
            raise Exception('Something went wrong, can not get the current cart quantity')

    def click_on_shopping_cart_icon(self):
        try:
            return self.web_utils.find_element(*self.shopping_cart_icon).click()
        except Exception:
            raise Exception('Something went wrong, can not get the shopping cart icon')

    def click_on_sort_container(self):
        try:
            self.web_utils.find_element(*self.sort_container).click()
            time.sleep(0.5)
        except Exception:
            raise Exception('Something went wrong, can not click on the sort container')

    def sort_high_to_low(self):
        try:
            self.click_on_sort_container()
            self.web_utils.find_element(*self.high_to_low).click()
            time.sleep(0.5)
        except Exception:
            raise Exception('Something went wrong trying to sort from high to low')

    def sort_z_to_a(self):
        try:
            self.click_on_sort_container()
            self.web_utils.find_element(*self.z_to_a).click()
            time.sleep(0.5)
        except Exception:
            raise Exception('Something went wrong trying to sort from z to a')

    def get_inventory_root(self):
        try:
            return self.web_utils.find_element(*self.inventory_list)
        except Exception:
            raise Exception('Something went wrong trying to get the root inventory element')

    def saving_items_data(self, root_element, callback_function):
        prices = []
        try:
            for item in root_element.find_elements(*self.inventory_list_elements):
                prices.append(callback_function(item))
            return prices
        except Exception:
            raise Exception('Something went wrong, can not get the children inventory elements')

    def saving_individual_price(self, item):
        try:
            return item.find_element(*self.inventory_item_price).text[1::]
        except Exception:
            raise Exception('Something went wrong trying to get the individual element price')

    def saving_individual_names(self, item):
        try:
            return item.find_element(*self.inventory_item).text
        except Exception:
            raise Exception('Something went wrong trying to get the individual element name')
