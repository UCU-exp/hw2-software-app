"""
database methods
"""

import mysql.connector
import dotenv as _dotenv
import os as _os
import typing as _typing

_dotenv.load_dotenv()

def pre_requirements() -> mysql.connector.connection_cext.CMySQLConnection:
	mydb = mysql.connector.connect(
		host=_os.environ.get('HOST'),
		user=_os.environ.get('ROOT_USER'),
		password=_os.environ.get('PASSWORD')
	)
	return mydb

def define_cursor(mydb: mysql.connector.connection_cext.CMySQLConnection) -> mysql.connector.cursor_cext.CMySQLCursor:
	mycursor = mydb.cursor()
	return mycursor

def create_database(cursor: mysql.connector.cursor_cext.CMySQLCursor) -> _typing.Union[str, None]:
	query = f"CREATE DATABASE {_os.environ.get('DB_NAME')}"
	try:
		cursor.execute(query)
		print(f'Database {_os.environ.get('DB_NAME')} created correctly')
	except Exception as e:
		print(f'Database exists or something else: {e}')

def create_tourists_info_table(cursor: mysql.connector.cursor_cext.CMySQLCursor) -> _typing.Union[str, None]:
	query = 'CREATE TABLE IF NOT EXISTS TouristInfo (fistName VARCHAR(22), lastName VARCHAR(20), phoneNumber VARCHAR(20) NOT NULL PRIMARY KEY, class INT, nickName VARCHAR(46), payment VARCHAR(4) NOT NULL);'
	try:
		cursor.execute(query)
		print(f'Table TouristInfo created correctly')
	except Exception as e:
		print(f"Table 'Tourists' exists or something else: {e}")

def create_tickets_table(cursor: mysql.connector.cursor_cext.CMySQLCursor) -> _typing.Union[str, None]:
	query = 'CREATE TABLE IF NOT EXISTS Tickets (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(12), registrateDate VARCHAR(12), groupNo INT PRIMARY KEY, startTime VARCHAR(6), endTime VARCHAR(6), duration INT);'
	try:
		cursor.execute(query)
		print(f'Table Tickets created correctly')
	except Exception as e:
		print(f"Table 'Tickets' exists or something else: {e}")

def create_catering_table(cursor: mysql.connector.cursor_cext.CMySQLCursor) -> _typing.Union[str, None]:
	query = 'CREATE TABLE IF NOT EXISTS Catering (mealType VARCHAR(42), drinksType VARCHAR(42));'
	try:
		cursor.execute(query)
		print(f'Table Catering created correctly')
	except Exception as e:
		print(f"Table 'Catering' exists or something else: {e}")

def create_fees_info_table(cursor: mysql.connector.cursor_cext.CMySQLCursor) -> _typing.Union[str, None]:
	query = "CREATE TABLE IF NOT EXISTS FeesInfo (id INT AUTO_INCREMENT PRIMARY KEY, label VARCHAR(32), aim VARCHAR(102), size INT NOT NULL);"
	try:
		cursor.execute(query)
		print(f'Table FeesInfo created correctly')
	except Exception as e:
		print(f"Table 'FeesInfo' exists or something else: {e}")


if __name__ == '__main__':
	mydb = pre_requirements()
	cursor = define_cursor(mydb)
	create_database(cursor)
