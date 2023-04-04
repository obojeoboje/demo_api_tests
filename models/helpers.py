import os
import requests
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('email')
PASSWORD = os.getenv('password')
URL = os.getenv('url')

base_url = URL


def data_create_user():
    data = {
        'name': 'Gandalf',
        'job': 'wizard'
    }
    return data


def data_edit_user():
    data = {
        'name': 'morpheus',
        'job': 'zion resident'
    }
    return data


def data_register_user():
    data = {
        'email': "eve.holt@reqres.in",
        'password': "pistol"
    }
    return data


def authorization():
    authorization = requests().post('/api/login', data={
        "email": LOGIN,
        "password": PASSWORD
    })
    cookie_value = authorization.cookies.get('token')
    token = {}
    if cookie_value is not None:
        token.update({"token": cookie_value})
    return token
