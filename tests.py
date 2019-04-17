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

user_1_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_1)
user_2_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_2)
user_3_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_3)
user_4_data = requests.post('http://localhost:3000/api/v2/create', params=payload_user_4)

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

print('U1: ' + user_1_guid + ', ' + user_1_address)
print('U2: ' + user_2_guid + ', ' + user_2_address)
print('U3: ' + user_3_guid + ', ' + user_3_address)
print('U4: ' + user_4_guid + ', ' + user_4_address)

# Outgoing payments between two users
payment_user_1 = requests.post('https://blockchain.info/merchant/' + user_1_guid + '/.')
print(payment_user_1.status_code)
print(payment_user_1.json())
# print('Status: ' + str(payment_user_1.status_code) + ', message: ' + payment_user_1.json())

# for i in range(1, 4):
#     user = 'user_' + str(i) + '_data'
#     if user.status_code == 200:
#         print(str('user_' + i + ' created successfully!'))
#     else:
#         print(str('user_' + i + ' creation failed!'))
# print(p.status_code)
# print(p.json())
# guid_data = p.json().get('guid')
# address_data = p.json().get('address')
# print(guid_data)
# print(address_data)

