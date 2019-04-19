import requests


def enable(guid, payload):
    try:
        user_data = requests.post('http://localhost:3000/merchant/' + guid + '/enableHD', params=payload)
        return user_data
    except requests.exceptions.SSLError:
        return "Connection refused"
