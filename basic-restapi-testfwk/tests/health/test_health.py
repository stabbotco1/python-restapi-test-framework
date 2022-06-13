import pytest
import requests
from config import SESSION, APP_URL, LOG

def test_health():
    LOG.info("test_health")
    #  the following is for convenience and a health library should be created
    response = SESSION.get(f'{APP_URL}/health')
    assert response.ok