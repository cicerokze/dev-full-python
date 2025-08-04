from .order_form import api_order_form_router
from .order_list import api_order_list_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(api_order_form_router)
api_router.include_router(api_order_list_router)