import os
import tempfile

import pytest

from app import app

@pytest.fixture
def client():
   #app.config['TESTING'] = True
   return app.test_client()

def test_homepage_displays(client):
    """When calling the default route the homepage should return."""

    returnvalue = client.get('/')
    assert b'Currently the list contains the following:' in returnvalue.data

def test_add_item(client):
    """When adding an item it should be in the list afterwards."""

    returnvalue = client.post('/addentry', data="Bananas")
    assert b'Bananas' in returnvalue.data