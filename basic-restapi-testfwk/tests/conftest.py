import requests
import pytest
from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD

# Define fixture to be used to authenticate for tests that require admin login authenticated and token
@pytest.fixture(scope="session") # declare fixture scope to test session
def login_as_admin():
    # 1. authenticate
    payload = {"username":ADMIN_USER, "password":ADMIN_PASSWORD}
    response = SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert response.ok

    access_token = response.json()["access_token"]
    # use yield instead of return to allow logout implementation later
    yield access_token
    
    # here is where code resumes and logs out later
    # This is needed to leave system as started
    