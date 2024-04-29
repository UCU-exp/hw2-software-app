"""
execute models
"""

from pydantic import BaseModel

class Catering(BaseModel):
	mealType: str
	drinksType: str

class FeesInfo(BaseModel):
	label: str
	aim: str
	size: int

class Ticket(BaseModel):
	type_execut: str
	registrateDate: str
	groupNo: int
	startTime: str
	endTime: str
	duration: int

class Tourist(BaseModel):
	fistName: str
	lastName: str
	phoneNumber: str
	class_execut: int
	nickName: str
	payment: str
