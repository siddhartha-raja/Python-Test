import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test if the home page loads."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_login_page(client):
    """Test if the login page exists."""
    rv = client.get('/login')
    # This will pass if you have a /login route in app.py
    assert rv.status_code == 200