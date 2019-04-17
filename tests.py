import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)

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
payload_balance_1 = {'password': payload_user_1.get('password'), 'api_code': payload_user_1.get('api_code')}
try:
    account_balance_1 = requests.get('http://localhost:3000/merchant/' + user_1_guid + '/balance', params=payload_balance_1)
except requests.exceptions.SSLError:
    print("Connection refused!")
print('[BALANCE] ' + account_balance_1.json().get('balance'))
print(account_balance_1.status_code)


"""
TEST FOR MAKING OUTGOING PAYMENTS
"""

# print(payload_payment_1.get('message'))
# print(payment_user_1.text)
# print(payment_user_1.get('tx_hash'))
# print(payment_user_1.get('notice'))
# print('Status: ' + str(payment_user_1.status_code) + ', message: ' + payment_user_1.json())


#

