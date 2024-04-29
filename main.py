"""
main configurations
"""

import fastapi as _fastapi
import dotenv as _dotenv

app = _fastapi.FastAPI()

_dotenv.load_dotenv()

@app.get('/')
def root_endpoint():
	return {'data': 'test_app'}
