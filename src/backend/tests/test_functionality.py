"""
Describing all functional tests in app.

Has a few method for testing some of user scripts.
"""
import requests
import utils

HOST = "http://localhost:8080/"
USER_MAIN_URL = "http://localhost:8080/users/"


def test_main_page_is_working():
    """
    Testing if main page is working.

    Asserted than `status_code` of response is not 200
    or returned text is not `Hello, world`
    """
    response = requests.get(HOST)

    assert response.status_code == 200, "Status code is not 200"
    assert response.text == "Hello, world"


def test_users_registration():
    """
    Create some users and test that they created properly.

    We will create two users with given `USERNAMES`.
    This test checks if response for creation is correct and that every user is
    saved to db.
    """

    USERNAMES = ('first', 'second')

    for username in USERNAMES:
        # Creating user with giver username and generated password
        creation_response = requests.post(
            USER_MAIN_URL,
            data={
                "username": username,
                "password": utils.weak_password_generator(username),
            },
        )
        # Asserting if response is propriate
        assert creation_response.status_code == 200, "Status code is not 200"
        assert username in creation_response.text, "Username is not in response"

    all_users_response = requests.get(USER_MAIN_URL)

    assert all_users_response.status_code == 200, "Status code is not 200"
    assert all(username in all_users_response.text for username in USERNAMES)
