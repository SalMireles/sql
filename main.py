from fastapi import FastAPI

from products.db.engine import DBSession, init_db
from products.db.models import DBProducts

app = FastAPI()


DB_FILE = "sqlite:///products.db"


@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)


@app.get("/")
def read_root():
    return "The server is running."


@app.get("/products")
def read_all_products():
    session = DBSession()
    products = session.query(DBProducts).all()
    return products
