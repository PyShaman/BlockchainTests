import requests


def create_wallet(payload):
    try:
        user_data = requests.post('http://localhost:3000/api/v2/create', params=payload)
        return user_data
    except requests.exceptions.SSLError:
        return "Connection refused"
