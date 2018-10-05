import sqlite3

def get_conn(db_name):
	conn = sqlite3.connect(db_name)
	conn.row_factory = sqlite3.Row
	return conn.cursor()
	
def get_items(table_name, db):
	db.execute('select * from %s' % table_name)
	return list(map(dict, db.fetchall()))
