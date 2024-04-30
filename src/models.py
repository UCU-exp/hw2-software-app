"""
execute models
"""

from pydantic import BaseModel

class Catering(BaseModel):
	"""
	Catering class
	"""
	mealType: str
	drinksType: str

class FeesInfo(BaseModel):
	"""
	FeesInfo class
	"""
	label: str
	aim: str
	size: int

class Ticket(BaseModel):
	"""
	Ticket class
	"""
	type_execut: str
	registrateDate: str
	groupNo: int
	startTime: str
	endTime: str
	duration: int

class Tourist(BaseModel):
	"""
	Tourist class
	"""
	firstName: str
	lastName: str
	phoneNumber: str
	class_execut: int
	nickName: str
	payment: str
