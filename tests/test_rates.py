"""
Test cases for testing getting currency data
    
- get currencies exchange rate by date
- Get Movements of currencies by date
    
"""
import pytest
from src import create_app
import logging

logger = logging.getLogger()

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG,
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)


@pytest.fixture
def client():
    test_app = create_app()
    test_app.config.from_object('config.TestingConfig')

    with test_app.test_client() as client:
        yield client


def test_home_page(client):
    """Test for home url """
    response = client.get('/')
    test_app = create_app()
    test_app.logger.info("getting response for home url")
    assert response.status_code == 200

#


def test_currency(client):
    """Test to get currency by date """

    data = {"business_date": "2023-01-24",
            "currency_code": "AFN",
            "exchange_rate": 88.9231,
            "id": 517
            }
    test_app = create_app()
    test_app.logger.info("getting response from currency url")

    res = client.get('/api/currencies/2023-01-24')
    assert res.status_code == 200
    assert res.json['rates'][0] == data


def test_movements(client):
    """ Test to calculate currency movements """
    data = {
        "country_name": "Albania",
        "currency_code": "ALL",
        "movement": -0.24
    }
    test_app = create_app()
    test_app.logger.info("Getting response from movements calculation url")
    res = client.get('/api/movements/2023-01-25')
    dat = []
    for d in dat:
        dat.append(res.json['movements'])
        if data in dat:
            test_app.logger.info(f"{data} in movements, hence test passing.")
            assert d == data
    assert res.status_code == 200
