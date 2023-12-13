from behave import step

from features.pages.cart_page import CartPage


@step("Tom sees the items correctly added to the cart")
def check_items_in_cart(context):
    context.current_page = CartPage(context.browser.driver)
    for item in context.items_and_prices:
        assert context.current_page.is_item_and_price_in_cart(item, context.items_and_prices[item])


@step("Tom clicks on checkout")
def check_items_in_cart(context):
    context.current_page.click_on_checkout()
