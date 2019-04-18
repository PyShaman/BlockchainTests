import pyping
import requests


def connection(server):
    r = pyping.ping(server)
    return r.ret_code

