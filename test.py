import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert b'Reservation' in rv.data

def test_reservation_form(client):
    rv = client.post('/reserve', data=dict(
        date='2024-09-01',
        time='19:00',
        guests=4
    ), follow_redirects=True)
    assert b'Reservation confirmed!' in rv.data
