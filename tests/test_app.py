import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test if the home page loads."""
    rv = client.get('/', follow_redirects=True)
    assert rv.status_code == 200

def test_login_page(client):
    """Test if the login page exists."""
    rv = client.get('/login')
    # This will pass if you have a /login route in app.py
    assert rv.status_code == 200


def test_registration_rejects_short_password(client):
    rv = client.post(
        '/register',
        data={'username': 'alice', 'password': 'short'},
    )

    assert rv.status_code == 200
    assert b'at least 8 characters' in rv.data


def test_registration_trims_username_and_allows_login(client):
    client.post(
        '/register',
        data={'username': ' alice ', 'password': 'correct-horse'},
    )

    rv = client.post(
        '/login',
        data={'username': 'alice', 'password': 'correct-horse'},
    )

    assert rv.status_code == 302
    assert rv.headers['Location'].endswith('/dashboard')