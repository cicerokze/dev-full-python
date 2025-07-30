from .home import home_router
from .orders import orders_router
from fastapi import APIRouter

frontend_router = APIRouter()
frontend_router.include_router(home_router)
# frontend_router.include_router(orders_router)