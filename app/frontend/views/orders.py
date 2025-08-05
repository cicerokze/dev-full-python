from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/frontend/templates")
view_orders_router = APIRouter()

app = FastAPI()

@app.post("/add-item", response_class=HTMLResponse, include_in_schema=False)
async def add_item(request: Request):
    return {"message": "Item added successfully"}

@view_orders_router.get("/orders", response_class=HTMLResponse, include_in_schema=False)
async def order_list(request: Request):
    return templates.TemplateResponse("order_list.html", {"request": request})

@view_orders_router.get("/order/{id}", response_class=HTMLResponse, include_in_schema=False)
async def order_detail(request: Request, id: int):
    return templates.TemplateResponse("order_detail.html", {"request": request, "id": id})

@view_orders_router.get("/order", response_class=HTMLResponse, include_in_schema=False)
async def order_form(request: Request):
    return templates.TemplateResponse("order_form.html", {"request": request}) 
