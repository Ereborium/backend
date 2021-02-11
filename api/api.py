from fastapi import APIRouter
from api.endpoints import example

api_router = APIRouter()
api_router.include_router(example.router)
