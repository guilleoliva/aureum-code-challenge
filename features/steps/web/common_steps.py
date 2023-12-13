from behave import step

from features.pages.inventory_page import InventoryPage
from features.pages.landing_page import LandingPage


@step("Tom goes to {app_name} Web APP login page")
def open_app(context, app_name):
    context.execute_steps(
        """
        Given a browser
    """
    )
    context.browser.driver.maximize_window()
    app_url = context.env_config["app_url"]
    landing_page = LandingPage(context.browser.driver, app_url)
    landing_page.open_app()
    context.current_page = landing_page
    assert app_url in landing_page.get_current_url()


@step("Tom logs in with his credentials")
def logs_in(context):
    context.current_page.logs_in(context.env_config["username"], context.env_config["password"])


@step("Tom sees the dashboard")
def dashboard_present(context):
    context.current_page = InventoryPage(context.browser.driver)
    assert context.current_page.is_burger_menu_present()


@step('Tom should see the "Swags Lab" icon present')
def logo_presence(context):
    assert context.current_page.is_swags_icon_present(), "The 'Swags Lab' icon was not present"


@step("Tom clicks on the Log in button")
def log_in_button(context):
    context.current_page.submit_login()


@step("Tom clicks on the shopping cart icon")
def click_shopping_cart(context):
    context.current_page.click_on_shopping_cart_icon()
