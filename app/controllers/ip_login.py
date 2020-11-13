from functools import wraps

from flask import request

# here one has to put all IPs of bots and any other that are going to be used to test this application
GOOD_IPS = ['212.90.63.164', '127.0.0.1']


def ip_login(a_func):

    @wraps(a_func)
    def wrapTheFunction(*args, **kwargs):
        ip = request.remote_addr
        if ip in GOOD_IPS:
            return a_func(*args, **kwargs)

    return wrapTheFunction
