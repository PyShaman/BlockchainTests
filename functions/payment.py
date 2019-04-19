import requests


def payment(guid, payload):
    try:
        payment_1_2 = requests.get('http://localhost:3000/merchant/' + guid + '/payment', params=payload)
        return payment_1_2
    except requests.exceptions.HTTPError:
        print("Connection refused! Status code: " + payment_1_2.status_code)