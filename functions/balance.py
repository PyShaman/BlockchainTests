import requests


def balance(guid, payload):
    try:
        account_balance = requests.get('http://localhost:3000/merchant/' + guid + '/balance', params=payload)
        return account_balance
    except requests.exceptions.SSLError:
        return "Connection refused! Status code: " + account_balance.status_code
