import requests
import allure
from allure_commons.types import Severity
from requests import Response
from pytest_voluptuous import S
from shemas.reqres import get_single_user_schema, \
    post_create_user_schema, \
    post_register_user_schema, \
    put_user_schema
from models.helpers import base_url, data_create_user, data_edit_user, data_register_user


@allure.parent_suite("API")
@allure.severity(Severity.CRITICAL)
@allure.suite("User")
@allure.title("Get single user")
def test_get_single_user():
    with allure.step('send get request'):
        response: Response = requests.get(base_url + "/api/users/2")

    with allure.step('check status code'):
        assert response.status_code == 200
    with allure.step('check schema'):
        assert response.json() == S(get_single_user_schema)
    with allure.step('check data'):
        assert response.json()['data']['id'] == 2
        assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
        assert response.json()['data']['first_name'] == 'Janet'
        assert response.json()['data']['last_name'] == 'Weaver'

@allure.parent_suite("API")
@allure.severity(Severity.MINOR)
@allure.suite("User")
@allure.title("Post single user")
def test_post_create_user():
    with allure.step('send post request'):
        create = requests.post(base_url + "/api/users", data_create_user())

    with allure.step('check status code'):
        assert create.status_code == 201
    with allure.step('check schema'):
        assert create.json() == S(post_create_user_schema)
    with allure.step('check data'):
        assert create.json()["name"] == data_create_user()['name']
        assert create.json()["job"] == data_create_user()['job']
        assert isinstance(create.json()["id"], str)
        assert isinstance(create.json()["createdAt"], str)

@allure.parent_suite("API")
@allure.severity(Severity.TRIVIAL)
@allure.suite("User")
@allure.title("Put single user")
def test_put_user():
    with allure.step('send put request'):
        update = requests.put(base_url + '/api/users/2', data_edit_user())

    with allure.step('check status code'):
        assert update.status_code == 200
    with allure.step('check schema'):
        assert update.json() == S(put_user_schema)
    with allure.step('check data'):
        assert update.json()['name'] == data_edit_user()['name']
        assert update.json()['job'] == data_edit_user()['job']

@allure.parent_suite("API")
@allure.severity(Severity.CRITICAL)
@allure.suite("User")
@allure.title("Delete single user")
def test_delete_user():
    with allure.step('send delete request'):
        result = requests.delete('https://reqres.in/api/users/2')

    with allure.step('check status code'):
        assert result.status_code == 204


@allure.parent_suite("API")
@allure.severity(Severity.NORMAL)
@allure.suite("User")
@allure.title("Post register single user")
def test_post_register_user():
    with allure.step('send post request'):
        register = requests.post(base_url + '/api/register', data_register_user())

    with allure.step('check status code'):
        assert register.status_code == 200
    with allure.step('check schema'):
        assert register.json() == S(post_register_user_schema)
    with allure.step('check data'):
        assert register.json()["id"] == 4
        assert isinstance(register.json()["id"], int)
        assert register.json()["token"] == "QpwL5tke4Pnpja7X4"
        assert isinstance(register.json()["token"], str)
