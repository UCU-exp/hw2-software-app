"""
main configurations
"""

import fastapi as _fastapi
import src.db_setup as _db_setup
import src.models as _models
import src.queries as _queries

app = _fastapi.FastAPI()

@app.get('/')
def root_endpoint():
	"""
	Get endpoint for testing
	"""
	return {'data': 'test_app'}

@app.get('/create-tourists')
def define_tourists_table():
	"""
	Get enpoint to define tourists table
	"""
	custom_query = _queries.init_tourists_table()
	status_ok = _db_setup.create_custom_table(custom_query)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'TouristsInfo' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-tickets')
def define_tickets_table():
	"""
	Get enpoint to define tickets table
	"""
	custom_query = _queries.init_tickets_table()
	status_ok = _db_setup.create_custom_table(custom_query)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'Tickets' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-catering')
def define_catering_table():
	"""
	Get enpoint to define catering table
	"""
	custom_query = _queries.init_catering_table()
	status_ok = _db_setup.create_custom_table(custom_query)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'Catering' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.get('/create-fees')
def define_fees_table():
	"""
	Get enpoint to define fees table
	"""
	custom_query = _queries.init_fees_table()
	status_ok = _db_setup.create_custom_table(custom_query)
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Table 'FeesInfo' created OK")
	return _fastapi.HTTPException(status_code=429, detail="Some error")

@app.post('/add-tourist')
def insert_tourist(tourist: _models.Tourist):
	"""
	Get enpoint to insert tourist into tourists table
	"""
	if _db_setup.find_tourist_by_phone(tourist.phoneNumber):
		custom_query = _queries.insert_tourist(tourist)
		status_ok = _db_setup.insert_into_custom_table(custom_query[0], custom_query[1])
		if status_ok:
			return _fastapi.HTTPException(status_code=200, detail="User added OK")
		return _fastapi.HTTPException(status_code=429, detail="Some error")
	else:
		return _fastapi.HTTPException(status_code=429, detail="User with this phone number found")

@app.post('/add-ticket')
def inset_ticket(ticket: _models.Ticket):
	"""
	Get enpoint to insert ticket into tickets table
	"""
	custom_query = _queries.insert_ticket(ticket)
	status_ok = _db_setup.insert_into_custom_table(ticket, custom_query[0], custom_query[1])
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Ticket added OK")
	return _fastapi.HTTPException(status_code=429, detail="Ticker with this group number found")

@app.post('/add-catering')
def insert_catering(catering: _models.Catering):
	"""
	Get enpoint to insert catering into catring table
	"""
	custom_query = _queries.insert_catering(catering)
	status_ok = _db_setup.insert_into_custom_table(catering, custom_query[0], custom_query[1])
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Catering added OK")
	return _fastapi.HTTPException(status_code=429, detail="Something went wrong")

@app.post('/add-fees')
def insert_fees(fees: _models.FeesInfo):
	"""
	Get enpoint to insert fees into fees table
	"""
	custom_query = _queries.insert_fees(fees)
	status_ok = _db_setup.insert_into_custom_table(fees, custom_query[0], custom_query[1])
	if status_ok:
		return _fastapi.HTTPException(status_code=200, detail="Fees added OK")
	return _fastapi.HTTPException(status_code=429, detail="Something went wrong")

@app.post('/update-entrie')
def update_entry(table_name: str, new_value: str, search_key: str, search_value: str):
	"""
	Get enpoint to update custon value into custom table
	"""
	if all([_db_setup.check_if_attribute_exists(table_name, search_key), _db_setup.check_if_value_exists(table_name, search_value)]):
		custon_query = _queries.update_value_in_table(table_name, new_value, search_key, search_value)
		status_ok = _db_setup.update_values_by_search_key_and_search_values(custon_query)
		if status_ok:
			return _fastapi.HTTPException(status_code=200, detail="Updated OK")
		return _fastapi.HTTPException(status_code=429, detail="Something went wrong")
	else:
		return _fastapi.HTTPException(status_code=429, detail="Attribute or value is not exists")

@app.delete('/delete-entrie')
def delete_entrie(table_name: str, search_key: str, search_value: str):
	"""
	Get enpoint to delete custon value from custom table
	"""
	if all([_db_setup.check_if_attribute_exists(table_name, search_key), _db_setup.check_if_value_exists(table_name, search_value)]):
		custom_query = _queries.delete_entry_from_table(table_name, search_key, search_value)
		status_ok = _db_setup.delete_entrie_from_table(custom_query)
		if status_ok:
			return _fastapi.HTTPException(status_code=200, detail="Entrie deleted OK")
		return _fastapi.HTTPException(status_code=429, detail="Something went wrong")
	else:
		return _fastapi.HTTPException(status_code=429, detail="Attribute or value is not exists")
