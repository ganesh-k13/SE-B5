import pytest
import pytest_flask
from flask import url_for

@pytest.mark.skip(reason="no way of currently testing this")
class TestApp:
	# User View Start
	def test_items_index(self, client):
		res = client.get(url_for('items_index'))
		assert res.status_code == 200
	#User View End
	