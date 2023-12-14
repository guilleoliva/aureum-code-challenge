from behave import step

from features.pages.check_out_complete_page import CheckOutComplete
from features.pages.check_out_step_one_page import CheckOutStepOne
from features.pages.check_out_step_two_page import CheckOutStepTwo


@step('Tom fills the checkout information with his information "{}" "{}" and postal code "{}"')
def fill_checkout_information(context, name, last_name, postal_code):
    context.current_page = CheckOutStepOne(context.browser.driver)
    context.current_page.fill_user_information(name, last_name, postal_code)


@step("Tom clicks on continue")
def clicks_on_continue(context):
    context.current_page.click_on_continue()


@step("Tom sees the checkout overview")
def checkout_overview(context):
    context.current_page = CheckOutStepTwo(context.browser.driver)
    assert context.current_page.is_payment_information_present()


@step("Tom confirm the subtotal price is correct")
def total_price(context):
    current_price = context.current_page.get_sub_total_price()
    saved_prices = 0
    for item in context.items_and_prices:
        saved_prices += float(context.items_and_prices[item])
    assert float(current_price) == saved_prices, f'Expected price {saved_prices}, current {current_price}'


@step("Tom clicks on finish to complete the purchase")
def complete_purchase(context):
    context.current_page.click_on_finish()


@step("Tom sees his purchase now is complete")
def purchase_complete(context):
    context.current_page = CheckOutComplete(context.browser.driver)
    assert context.current_page.is_thank_you_message_present()
