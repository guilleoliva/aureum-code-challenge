import json

import requests
from behave import *

from utils.api_utils import get_access_token, raise_http_error, requests_get

requests.packages.urllib3.disable_warnings()




@step("the user is told the request was unauthorized")
@step("the user is informed that the request to refresh the token was unauthorized")
@step("the user is told their password is incorrect")
def verify_request_status_unauthorized(context):
    assert (
            context.response.status_code == 401
    ), "Expected status code 401, current " + str(context.response.status_code)
    assert context.response.reason == "Unauthorized", (
            "Expected reason unauthorized, current " + context.response.reason
    )


@step("the user is told the request was forbidden")
def verify_request_status_forbidden(context):
    assert (
            context.response.status_code == 403
    ), "Expected status code 403, current " + str(context.response.status_code)
    assert context.response.reason == "Forbidden", (
            "Expected reason forbidden, current " + context.response.reason
    )


@step("the user is told the get pet request was not found")
def verify_request_status_not_found(context):
    assert (
            context.response.status_code == 404
    ), "Expected status code 404, current " + str(context.response.status_code)
    assert context.response.reason == "Not Found", (
            "Expected reason Not Found, current " + context.response.reason
    )


@step("the user is told the request to create was successful")
@step("the user is told the get pet request was successful")
@step("the user is told the request to update was successful")
@step("the user is told the request to delete was successful")
def create_entity_response(context):
    assert (
            context.response.status_code == 200
    ), f"Expected status code 200, current {context.response.status_code}"
    assert (
            context.response.reason == "OK"
    ), f"Expected reason OK, current {context.response.reason}"


@step("the user is told the request was successful")
def request_success(context):
    assert (
            context.response.status_code == 201
    ), f"Expected status code 201, current {context.response.status_code}"
    assert (
            context.response.reason == "Created"
    ), f"Expected reason Created, current {context.response.reason}"


def verify_request_status(context, status, reason):
    assert context.response.status_code == status, (
            f"Expected status code "
            + {status}
            + ", current "
            + {context.response.status_code}
    )
    assert context.response.reason == reason, (
            f"Expected reason " + {reason} + ", current " + {context.response.reason}
    )
