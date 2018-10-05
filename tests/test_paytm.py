import pytest
import pytest_flask
from flask import url_for

@pytest.mark.skip(reason="no way of currently testing this")
class TestApp:

	# Paytm Start
	def test_selectpayment(self, client):
		# https://github.com/pytest-dev/pytest-flask/issues/7
		res = client.get(url_for('selectpayment'))
		assert res.status_code == 200
	# Paytm End 