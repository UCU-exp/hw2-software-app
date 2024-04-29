"""
database methods
"""

import dotenv as _dotenv
import mysql.connector
import os as _os
import src.models as _models

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

def create_tourists_info_table() -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = """
	CREATE TABLE IF NOT EXISTS TouristInfo 
		(
			fistName VARCHAR(22), 
			lastName VARCHAR(20), 
			phoneNumber VARCHAR(20) NOT NULL PRIMARY KEY, 
			class INT, 
			nickName VARCHAR(46), 
			payment VARCHAR(4) NOT NULL
		);
	"""
	cursor.execute(query)
	conn.close()
	return True

def create_tickets_table() -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = """
	CREATE TABLE IF NOT EXISTS Tickets 
		(
			id INT AUTO_INCREMENT PRIMARY KEY, 
			type VARCHAR(12), 
			registrateDate VARCHAR(12), 
			groupNo INT, 
			startTime VARCHAR(6), 
			endTime VARCHAR(6), 
			duration INT
		);
	"""
	cursor.execute(query)
	conn.close()
	return True

def create_catering_table() -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = """
	CREATE TABLE IF NOT EXISTS Catering 
		(
			mealType VARCHAR(42), 
			drinksType VARCHAR(42)
		);
	"""
	cursor.execute(query)
	conn.close()
	return True

def create_fees_info_table() -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = """
	CREATE TABLE IF NOT EXISTS FeesInfo 
		(
			id INT AUTO_INCREMENT PRIMARY KEY, 
			label VARCHAR(32), 
			aim VARCHAR(102), 
			size INT NOT NULL
		);
	"""
	cursor.execute(query)
	conn.close()
	return True

def insert_into_tourists_table(tourist: _models.Tourist) -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = f"""
	INSERT INTO TouristInfo
		(firstName, lastName, phoneNumber, class, nickName, payment)
		VALUES ({tourist.fistName}, {tourist.lastName}, {tourist.phoneNumber}, {tourist.class_execut}, {tourist.nickName}, {tourist.payment});
	"""
	cursor.execute(query)
	conn.close()
	return True

def insert_into_tickets_table(ticket: _models.Ticket) -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = f"""
	INSERT INTO Tickets
		(id, type, registrateDate, groupNo, startTime, endTime, duration)
		VALUES ({ticket.type_execut}, {ticket.registrateDate}, {ticket.groupNo}, {ticket.startTime}, {ticket.startTime}, {ticket.endTime}, {ticket.duration});
	"""
	cursor.execute(query)
	conn.close()
	return True

def insert_into_catering_table(catering: _models.Catering) -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = f"""
	INSERT INTO Catering
		(mealType, drinksType)
		VALUES ({catering.mealType}, {catering.drinksType});
	"""
	cursor.execute(query)
	conn.close()
	return True

def insert_into_fees_table(fees: _models.FeesInfo) -> bool:
	conn = connect()
	cursor = conn.cursor()
	query = f"""
	INSERT INTO FeesInfo
		(id, label, aim, size)
		VALUES ({fees.label}, {fees.aim}, {fees.size});
	"""
	cursor.execute(query)
	conn.close()
	return True
