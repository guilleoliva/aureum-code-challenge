from behave import *


@step('Tom inputs his credentials as "{}"')
def input_credentials(context, user_type):
    try:
        context.current_page.logs_in(context.users[user_type]['user_name'], context.users[user_type]['password'])
    except Exception:
        raise Exception(f'The User type "{user_type}" is not available inside the config file')


@step('Tom inputs an incorrect password as "{}"')
def input_wrong_password(context, user_type):
    try:
        context.current_page.logs_in(context.users[user_type]['user_name'], 'WRONG_PASSWORD')
    except Exception:
        raise Exception(f'The User type "{user_type}" is not available inside the config file')


@step("Tom sees the incorrect user/password message")
def incorrect_credentials(context):
    assert context.current_page.login_error_message(
        'Username and password do not match any user in this service'
    ), f'Can not find the expected message'


@step("Tom clicks on the burger menu")
def click_burger_menu(context):
    context.current_page.click_on_burger_menu()


@step("Tom clicks on Log out")
def log_out(context):
    context.current_page.click_on_log_out()


@step("Tom logs out correctly")
def logs_out_correctly(context):
    expected_url = context.env_config["app_url"]
    current_url = context.current_page.get_current_url()
    assert current_url == expected_url, f'Expected page {expected_url}, current {current_url}'
