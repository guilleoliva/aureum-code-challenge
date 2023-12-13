import json

import requests
from behave import step

from utils.api_utils import get_access_token, raise_http_error, requests_get

requests.packages.urllib3.disable_warnings()


@step("the Aereum application is running")
def Aereum_health(context):
    response = requests_get(context, "/web/health")
    if response.status_code == 200:
        status = response.json()["status"]
        assert "Healthy" in status, "The application is not running properly"
    else:
        raise_http_error(response)
