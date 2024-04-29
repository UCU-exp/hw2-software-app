"""
database queries
"""

import src.models as _models


def init_tourists_table():
	query = """
	CREATE TABLE IF NOT EXISTS TouristInfo 
		(
			firstName VARCHAR(22),
			lastName VARCHAR(20),
			phoneNumber VARCHAR(20) NOT NULL PRIMARY KEY,
			class INT,
			nickName VARCHAR(46),
			payment VARCHAR(4) NOT NULL
		);
	"""
	return query

def init_tickets_table():
	query = """
	CREATE TABLE IF NOT EXISTS Tickets
		(
			id INT AUTO_INCREMENT PRIMARY KEY,
			type_execut VARCHAR(12),
			registrateDate VARCHAR(12),
			groupNo INT,
			startTime VARCHAR(6),
			endTime VARCHAR(6),
			duration INT
		);
	"""
	return query

def init_catering_table():
	query = """
	CREATE TABLE IF NOT EXISTS Catering 
		(
			mealType VARCHAR(42), 
			drinksType VARCHAR(42)
		);
	"""
	return query

def init_fees_table():
	query = """
	CREATE TABLE IF NOT EXISTS FeesInfo 
		(
			id INT AUTO_INCREMENT PRIMARY KEY,
			label VARCHAR(32), 
			aim VARCHAR(102), 
			size INT NOT NULL
		);
	"""
	return query

def insert_tourist(tourist: _models.Tourist):
	query = f"""
	INSERT INTO TouristInfo
		(firstName, lastName, phoneNumber, class, nickName, payment)
		VALUES (%s, %s, %s, %s, %s, %s);
	"""
	values = (tourist.firstName, tourist.lastName, tourist.phoneNumber, tourist.class_execut, tourist.nickName, tourist.payment)
	return (query, values)

def insert_ticket(ticket: _models.Ticket):
	query = f"""
	INSERT INTO Tickets
		(type_execut, registrateDate, groupNo, startTime, endTime, duration)
		VALUES (%s, %s, %s, %s, %s, %s);
	"""
	values = (ticket.type_execut, ticket.registrateDate, ticket.groupNo, ticket.startTime, ticket.endTime, ticket.duration)
	return (query, values)

def insert_catering(catering: _models.Catering):
	query = f"""
	INSERT INTO Catering
		(mealType, drinksType)
		VALUES (%s, %s);
	"""
	values = (catering.mealType, catering.drinksType)
	return (query, values)

def insert_fees(fees: _models.FeesInfo):
	query = f"""
	INSERT INTO FeesInfo
		(label, aim, size)
		VALUES (%s, %s, %s);
	"""
	values = (fees.label, fees.aim, fees.size)
	return (query, values)
