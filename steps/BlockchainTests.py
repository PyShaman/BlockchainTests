from behave import *
from functions.balance import balance
from functions.hd import enable
from functions.ping import check
from functions.create import create_wallet
from functions.payment import payment


payload_user_1 = {'password': 'password_user_1',
                  'api_code': 'api_code_user_1',
                  'label': 'Main Adress',
                  'email': 'user_1@mail.com'}
payload_user_2 = {'password': 'password_user_2',
                  'api_code': 'api_code_user_2',
                  'label': 'Main Adress',
                  'email': 'user_2@mail.com'}
payload_user_3 = {'password': 'password_user_3',
                  'api_code': 'api_code_user_3',
                  'label': 'Main Adress',
                  'email': 'user_3@mail.com'}
payload_user_4 = {'password': 'password_user_4',
                  'api_code': 'api_code_user_4',
                  'label': 'Main Adress',
                  'email': 'user_4@mail.com'}


@given("I am connected to Blockchain Wallet API")
def step_1(context):
    assert check() is True


@when("I create new wallets")
def step_2(context):
    wallet_1 = create_wallet(payload_user_1)
    wallet_2 = create_wallet(payload_user_2)
    wallet_3 = create_wallet(payload_user_3)
    wallet_4 = create_wallet(payload_user_4)
    status_1 = wallet_1.status_code
    status_2 = wallet_2.status_code
    status_3 = wallet_3.status_code
    status_4 = wallet_4.status_code
    wallet_list = [wallet_1, wallet_2, wallet_3, wallet_4]
    status_list = [status_1, status_2, status_3, status_4]
    return wallet_list, status_list


@Then("New wallets are created")
def step_3(context):
    wallet_list, status_list = step_2(context)
    assert status_list[0] is 200
    assert status_list[1] is 200
    assert status_list[2] is 200
    assert status_list[3] is 200


@When("I enable HD for wallets")
def step_4(context):
    wallet_list, status_list = step_2(context)
    guid_1 = wallet_list[0].json().get('guid')
    guid_2 = wallet_list[1].json().get('guid')
    guid_3 = wallet_list[2].json().get('guid')
    guid_4 = wallet_list[3].json().get('guid')
    hd_1 = enable(guid_1, {'password': payload_user_1.get('password')})
    hd_2 = enable(guid_2, {'password': payload_user_2.get('password')})
    hd_3 = enable(guid_3, {'password': payload_user_3.get('password')})
    hd_4 = enable(guid_4, {'password': payload_user_4.get('password')})
    hd_list = [hd_1, hd_2, hd_3, hd_4]
    return hd_list


@Then("Wallets have enabled HD")
def step_5(context):
    hd_list = step_4(context)
    assert hd_list[0].json().get('extendedPublicKey') is not None
    assert hd_list[1].json().get('extendedPublicKey') is not None
    assert hd_list[2].json().get('extendedPublicKey') is not None
    assert hd_list[3].json().get('extendedPublicKey') is not None


@When("I check balance of account")
def step_6(context):
    wallet_list, status_list = step_2(context)
    payload_balance_1 = {'password': payload_user_1.get('password'),
                         'api_code': payload_user_1.get('api_code')}
    wallet_1_guid = wallet_list[0].json().get('guid')
    payload_balance_2 = {'password': payload_user_2.get('password'),
                         'api_code': payload_user_2.get('api_code')}
    wallet_2_guid = wallet_list[1].json().get('guid')
    payload_balance_3 = {'password': payload_user_3.get('password'),
                         'api_code': payload_user_3.get('api_code')}
    wallet_3_guid = wallet_list[2].json().get('guid')
    payload_balance_4 = {'password': payload_user_4.get('password'),
                         'api_code': payload_user_4.get('api_code')}
    wallet_4_guid = wallet_list[3].json().get('guid')

    wallet_1_balance = balance(wallet_1_guid, payload_balance_1)
    wallet_2_balance = balance(wallet_2_guid, payload_balance_2)
    wallet_3_balance = balance(wallet_3_guid, payload_balance_3)
    wallet_4_balance = balance(wallet_4_guid, payload_balance_4)

    wallet_balance_list = [wallet_1_balance, wallet_2_balance, wallet_3_balance, wallet_4_balance]
    return wallet_balance_list


@Then("Account balance is returned")
def step_7(context):
    wallet_balance_list = step_6(context)
    assert wallet_balance_list[0].json().get('balance') is not None
    assert wallet_balance_list[1].json().get('balance') is not None
    assert wallet_balance_list[2].json().get('balance') is not None
    assert wallet_balance_list[3].json().get('balance') is not None


@Then("Account balance is printed")
def step_8(context):
    wallet_balance_list = step_6(context)
    print('[BALANCE_1] ' + str(wallet_balance_list[0].json().get('balance')))
    print('[BALANCE_2] ' + str(wallet_balance_list[1].json().get('balance')))
    print('[BALANCE_3] ' + str(wallet_balance_list[2].json().get('balance')))
    print('[BALANCE_4] ' + str(wallet_balance_list[3].json().get('balance')))
    print("--- END ---")


@When("I perform outgoing payment")
def step_9(context):
    wallet_list, status_list = step_2(context)
    hd_list = step_4(context)
    wallet_1_guid = wallet_list[0].json().get('guid')
    wallet_2_address = wallet_list[1].json().get('address')
    from_1 = hd_list[0].json().get('index')
    payload_payment_1_2 = {'password': payload_user_1.get('password'),
                           'to': wallet_2_address,
                           'amount': 5000,
                           'from': from_1,
                           'fee_per_byte': 10}

    return payment(wallet_1_guid, payload_payment_1_2)


@Then("Amount of bitcoins is transferred between accounts")
def step_10(context):
    account_payment = step_7(context)
    print(account_payment)
    print("--- END ---")
