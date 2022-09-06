export PYENV_VERSION=3.8.10

install:
	@pip install --upgrade pip
	@pip install poetry==1.1.12
	@poetry update
	@poetry install
	@poetry shell
run:
	uvicorn main:app --reload

get:
	@curl -X GET http://127.0.0.1:8000/$(endpoint)