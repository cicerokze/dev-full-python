from typing import Optional
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.core.database import orders_collection

templates = Jinja2Templates(directory="app/frontend/templates")
view_home_router = APIRouter()

@view_home_router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request, status: Optional[str] = None):

    """
        Home page that lists all orders.
        The response is unpaginated and limited to 10 results.
    """

    orders = await orders_collection.find().to_list(10)

    # Filter orders based on the selected status (if any)
    filtered_orders = [order for order in orders if not status or order['cutomer_name'].lower() == status.lower()]

    return templates.TemplateResponse("home.html", {"request": request, "orders": orders})

    