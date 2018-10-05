import sys
import pytest
from flaskr.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app