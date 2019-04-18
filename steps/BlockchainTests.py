from behave import *

from functions import connection_check


@given("I am connected to Blockchain Wallet API")
def step_impl(context):
    assert connection_check.connection("http://127.0.0.1:3000/") == 0
    # https://stackoverflow.com/questions/2953462/pinging-servers-in-python