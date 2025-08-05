from .home import view_home_router
from .orders import view_orders_router
from fastapi import APIRouter

view_router = APIRouter()
view_router.include_router(view_home_router)
view_router.include_router(view_orders_router)