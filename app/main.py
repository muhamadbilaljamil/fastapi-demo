from fastapi import FastAPI
from .routes.user import user

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

app.include_router(user, tags=["Users"])