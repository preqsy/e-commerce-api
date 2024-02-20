from fastapi import FastAPI
from endpoints import auth_users, products, auth
from app.database import engine
from app import models

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=products.router)
app.include_router(router=auth_users.router)
app.include_router(router=auth.router)