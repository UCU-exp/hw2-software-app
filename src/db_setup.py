"""
database methods
"""

import dotenv as _dotenv
import mysql.connector
import os as _os
import src.models as _models
import src.queries as _queries

_dotenv.load_dotenv()

MYSQL_HOST = _os.environ.get('HOST')
MYSQL_USER = _os.environ.get('ROOT_USER')
MYSQL_PASSWORD = _os.environ.get('PASSWORD')
MYSQL_DB = _os.environ.get('DB_NAME')

def connect():
	return mysql.connector.connect(
		host=MYSQL_HOST,
		user=MYSQL_USER,
		password=MYSQL_PASSWORD,
		database=MYSQL_DB
	)

def create_custom_table(query: str) -> bool:
	conn = connect()
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()
	conn.close()
	return True

def insert_into_custom_table(tourist: _models.Tourist, query: str, values: tuple) -> bool:
	conn = connect()
	cursor = conn.cursor()
	cursor.execute(query, values)
	conn.commit()
	conn.close()
	return True
