import requests

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

"""
CREATE NEW USERS
"""
try:
    user_1_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_1)
except requests.exceptions.SSLError:
    print("Connection refused")
try:
    user_2_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_2)
except requests.exceptions.SSLError:
    print("Connection refused")
try:
    user_3_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_3)
except requests.exceptions.SSLError:
    print("Connection refused")
try:
    user_4_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_4)
except requests.exceptions.SSLError:
    print("Connection refused")

# user_2_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_2)
# user_3_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_3)
# user_4_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_4)

"""
TEST FOR CHECKING IF USER IS CREATED SUCCESSFULLY
"""
# Test 1 - check if account is created - by status code
print(user_1_data.status_code)
assert user_1_data.status_code == 200
print(user_2_data.status_code)
assert user_2_data.status_code == 200
print(user_3_data.status_code)
assert user_3_data.status_code == 200
print(user_4_data.status_code)
assert user_4_data.status_code == 200


# User data https://www.blockchain.com/api/blockchain_wallet_api
user_1_guid = user_1_data.json().get('guid')
user_1_address = user_1_data.json().get('address')
user_2_guid = user_2_data.json().get('guid')
user_2_address = user_2_data.json().get('address')
user_3_guid = user_3_data.json().get('guid')
user_3_address = user_3_data.json().get('address')
user_4_guid = user_4_data.json().get('guid')
user_4_address = user_4_data.json().get('address')

print('[U1] guid: ' + user_1_guid + ', address: ' + user_1_address)
print('[U2] guid: ' + user_2_guid + ', address: ' + user_2_address)
print('[U3] guid: ' + user_3_guid + ', address: ' + user_3_address)
print('[U4] guid: ' + user_4_guid + ', address: ' + user_4_address)

"""
TEST FOR CHECKING BALANCE
"""
# Check balance
payload_balance_1 = {'password': payload_user_1.get('password'),
                     'api_code': payload_user_1.get('api_code')}
payload_balance_2 = {'password': payload_user_2.get('password'),
                     'api_code': payload_user_2.get('api_code')}
payload_balance_3 = {'password': payload_user_3.get('password'),
                     'api_code': payload_user_3.get('api_code')}
payload_balance_4 = {'password': payload_user_4.get('password'),
                     'api_code': payload_user_4.get('api_code')}
try:
    account_balance_1 = requests.get('http://localhost:3000/merchant/' + user_1_guid + '/balance',
                                     params=payload_balance_1)
except requests.exceptions.SSLError:
    print("Connection refused! Status code: " + account_balance_1.status_code)
try:
    account_balance_2 = requests.get('http://localhost:3000/merchant/' + user_2_guid + '/balance',
                                     params=payload_balance_2)
except requests.exceptions.SSLError:
    print("Connection refused! Status code: " + account_balance_2.status_code)
try:
    account_balance_3 = requests.get('http://localhost:3000/merchant/' + user_3_guid + '/balance',
                                     params=payload_balance_3)
except requests.exceptions.SSLError:
    print("Connection refused! Status code: " + account_balance_3.status_code)
try:
    account_balance_4 = requests.get('http://localhost:3000/merchant/' + user_4_guid + '/balance',
                                     params=payload_balance_4)
except requests.exceptions.SSLError:
    print("Connection refused! Status code: " + account_balance_4.status_code)
print('[BALANCE_1] ' + str(account_balance_1.json().get('balance')))
print('[BALANCE_2] ' + str(account_balance_2.json().get('balance')))
print('[BALANCE_3] ' + str(account_balance_3.json().get('balance')))
print('[BALANCE_4] ' + str(account_balance_4.json().get('balance')))


"""
TEST FOR MAKING OUTGOING PAYMENTS
http://localhost:3000/merchant/$guid/payment?password=$main_password&second_password=$second_password&to=$address&amount=$amount&from=$from&fee=$fee
$main_password Your Main Blockchain Wallet password
$second_password Your second Blockchain Wallet password if double encryption is enabled.
$to Recipient Bitcoin Address.
$amount Amount to send in satoshi.
$from Send from a specific Bitcoin Address (Optional)
$fee Transaction fee value in satoshi (Must be greater than default fee) (Optional)
"""
payload_payment_1_2 = {'password': payload_user_1.get('password'),
                       'to': user_2_address,
                       'amount': 5000,
                       'fee': 10}

try:
    payment_1_2 = requests.get('http://localhost:3000/merchant/' + user_1_guid + '/payment',
                               params=payload_payment_1_2)
except requests.exceptions.HTTPError:
    print("Connection refused! Status code: " + payment_1_2.status_code)

print(payment_1_2.status_code)
print(payment_1_2.json().get('message'), payment_1_2.json().get('tx_hash'), payment_1_2.json().get('notice'))
# print(payload_payment_1.get('message'))
# print(payment_user_1.text)
# print(payment_user_1.get('tx_hash'))
# print(payment_user_1.get('notice'))
# print('Status: ' + str(payment_user_1.status_code) + ', message: ' + payment_user_1.json())

