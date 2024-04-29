"""
main configurations
"""

import fastapi as _fastapi
import src.db_setup as _db_setup
import src.models as _models

app = _fastapi.FastAPI()

@app.get('/')
def root_endpoint():
	return {'data': 'test_app'}

@app.get('/create-tourists')
def define_tourists_table():
	status_ok = _db_setup.create_tourists_info_table()
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'TouristsInfo' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-tickets')
def define_tickets_table():
	status_ok = _db_setup.create_tickets_table()
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'Tickets' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-catering')
def define_catering_table():
	status_ok = _db_setup.create_catering_table()
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'Catering' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-fees')
def define_tickets_table():
	status_ok = _db_setup.create_fees_info_table()
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'FeesInfo' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.post('/add-tourist')
def insert_tourist(tourist: _models.Tourist):
	status_ok = _db_setup.insert_into_tourists_table(tourist)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="User added OK")
	return _fastapi.HTTPException(status_code=429, detail="User with this phone number found")

@app.post('/add-ticket')
def inset_ticket(ticket: _models.Ticket):
	status_ok = _db_setup.insert_into_tickets_table(ticket)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Ticket added OK")
	return _fastapi.HTTPException(status_code=429, detail="Ticker with this group number found")

@app.post('/add-catering')
def insert_catering(catering: _models.Catering):
	status_ok = _db_setup.insert_into_catering_table(catering)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Catering added OK")
	return _fastapi.HTTPException(status_code=429, detail="Something went wrong")

@app.post('/add-fees')
def insert_fees(fees: _models.FeesInfo):
	status_ok = _db_setup.insert_into_fees_table(fees)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Fees added OK")
	return _fastapi.HTTPException(status_code=429, detail="Something went wrong")
