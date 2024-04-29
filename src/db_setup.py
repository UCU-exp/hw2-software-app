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

def insert_into_custom_table(query: str, values: tuple) -> bool:
	conn = connect()
	cursor = conn.cursor()
	cursor.execute(query, values)
	conn.commit()
	conn.close()
	return True

def update_values_by_search_key_and_search_values(query: str) -> bool:
	conn = connect()
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()
	conn.close()
	return True

def delete_entrie_from_table(query: str) -> bool:
	conn = connect()
	cursor = conn.cursor()
	cursor.execute(query)
	conn.commit()
	conn.close()
	return True

def find_tourist_by_phone(phone: str) -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = 'SELECT * FROM TouristInfo;'
	cursor.execute(query)
	results = cursor.fetchall()
	for item in results:
		if phone == item[2]:
			conn.commit()
			conn.close()
			return False
	conn.commit()
	conn.close()
	return True

def check_if_attribute_exists(table_name: str, search_key: str):
	conn = connect()
	cursor = conn.cursor()
	query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';"
	cursor.execute(query)
	column_names = cursor.fetchall()
	attributes = [i[0] for i in column_names][:len(column_names) // 2]
	if search_key in attributes:
		conn.commit()
		conn.close()
		return True
	conn.commit()
	conn.close()
	return False

def check_if_value_exists(table_name: str,  search_value: str):
	conn = connect()
	cursor = conn.cursor()
	query = f"SELECT * FROM {table_name};"
	cursor.execute(query)
	all_entries = cursor.fetchall()
	for item in all_entries:
		for entry in item:
			if entry == search_value:
				conn.commit()
				conn.close()
				return True
	conn.commit()
	conn.close()
	return False
