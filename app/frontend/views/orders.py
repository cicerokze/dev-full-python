from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/frontend/templates")
view_orders_router = APIRouter()

@view_orders_router.get("/orders", response_class=HTMLResponse)
async def order_list(request: Request):
    return templates.TemplateResponse("order_list.html", {"request": request})

@view_orders_router.get("/order/{order_id}", response_class=HTMLResponse)
async def order_detail(request: Request, order_id: int):
    return templates.TemplateResponse("order_detail.html", {"request": request, "order_id": order_id})

@view_orders_router.get("/order", response_class=HTMLResponse)
async def order_form(request: Request):
    return templates.TemplateResponse("order_form.html", {"request": request}) 
