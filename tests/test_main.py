import pytest
import sys
import os
## Change the root directory of the test file to import app
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}
