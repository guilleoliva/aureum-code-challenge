from behave import step

from features.pages.inventory_page import InventoryPage


@step("Tom wants to add the following items to his cart")
def add_item_to_cart(context):
    context.items_and_prices = {}
    for row in context.table:
        context.items_and_prices[row['Item Name']] = context.current_page.add_item_to_cart(row['Item Name'])


@step('Tom sees the shopping cart icon shows the "{}" items added')
def sees_cart_item(context, quantity):
    cart_qty = context.current_page.get_cart_item_quantity()
    assert (
        context.current_page.get_cart_item_quantity() == quantity
    ), f"Expected cart quantity {quantity}, current {cart_qty}"


@step('Tom clicks on sort items by price "{}"')
def sort_high_low(context, sort_type):
    sort = {'high to low': context.current_page.sort_high_to_low}
    context.sort_type = sort_type
    sort[sort_type]()


@step("Tom sees all the prices with no order")
def save_current_prices(context):
    context.current_page = InventoryPage(context.browser.driver)
    context.before_sort_prices = []
    context.before_sort_prices = context.current_page.saving_items_data(
        context.current_page.get_inventory_root(), context.current_page.saving_individual_price
    )


@step("Tom sees the items prices now are sorted correctly")
def sorted_correctly(context):
    context.sorted_prices = []
    sorting_data = {'high to low': sorted(context.before_sort_prices, key=float, reverse=True)}
    context.sorted_prices = context.current_page.saving_items_data(
        context.current_page.get_inventory_root(), context.current_page.saving_individual_price
    )
    saved_sorted = sorting_data[context.sort_type]
    assert context.sorted_prices == saved_sorted, f"Expected prices {saved_sorted}, current {context.sorted_prices}"


@step("Tom sees all the names with no order")
def save_names(context):
    context.current_page = InventoryPage(context.browser.driver)
    context.before_sort_names = []
    context.before_sort_names = context.current_page.saving_items_data(
        context.current_page.get_inventory_root(), context.current_page.saving_individual_names
    )


@step('Tom clicks on sort items by name "{}"')
def sort_by_name(context, sort_type):
    sort = {'Z to A': context.current_page.sort_z_to_a}
    context.sort_type = sort_type
    sort[sort_type]()


@step("Tom sees the items names now are sorted correctly")
def names_sorted(context):
    context.sorted_names = []
    sorting_data = {'Z to A': sorted(context.before_sort_names, reverse=True)}
    context.sorted_names = context.current_page.saving_items_data(
        context.current_page.get_inventory_root(), context.current_page.saving_individual_names
    )
    saved_sorted = sorting_data[context.sort_type]
    assert context.sorted_names == saved_sorted, f"Expected prices {saved_sorted}, current {context.sorted_names}"
