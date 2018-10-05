import pytest
import pytest_flask
from flask import url_for

class TestApp:

	# Canteen View Start
	def test_index(self, client):
		res = client.get(url_for('owner_index'))
		assert res.status_code == 200
	
	def test_elements(self, client):
		res = client.get(url_for('elements'))
		assert res.status_code == 200
	
	def test_panels(self, client):
		res = client.get(url_for('panels'))
		assert res.status_code == 200
		
	def test_page_profile(self, client):
		res = client.get(url_for('page_profile'))
		assert res.status_code == 200
		
	def test_page_login(self, client):
		res = client.get(url_for('page_login'))
		assert res.status_code == 200
		
	def test_page_lockscreen(self, client):
		res = client.get(url_for('page_lockscreen'))
		assert res.status_code == 200
		
	def test_charts(self, client):
		res = client.get(url_for('charts'))
		assert res.status_code == 200
		
	def test_notifications(self, client):
		res = client.get(url_for('notifications'))
		assert res.status_code == 200
		
	def test_tables(self, client):
		res = client.get(url_for('tables'))
		assert res.status_code == 200
		
	def test_icons(self, client):
		res = client.get(url_for('icons'))
		assert res.status_code == 200
	
	def test_typography(self, client):
		res = client.get(url_for('typography'))
		assert res.status_code == 200
	# Canteen View Start

	# User View Start
	def test_items_index(self, client):
		res = client.get(url_for('items_index'))
		assert res.status_code == 200
	#User View End
	