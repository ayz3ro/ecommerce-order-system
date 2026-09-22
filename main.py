from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.router import api_router
from core.exceptions import AppException
from core.exceptions.handlers import app_exception_handler

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )

app.add_exception_handler(AppException, app_exception_handler, )

app.include_router(api_router)
