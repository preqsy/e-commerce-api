from fastapi import FastAPI
from endpoints import products, users
from app.database import engine
from app import models

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=products.router)
app.include_router(router=users.router)