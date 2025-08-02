from fastapi import FastAPI, APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.dependencies import get_order_usecase
from app.features.order.models.order_model import OrderModel, ItemModel

from app.features.order.usecases import uc_order_form

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

templates = Jinja2Templates(directory="app/frontend/templates")

api_order_form_router = APIRouter()

@api_order_form_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"request": request}
    )


@api_order_form_router.post("/order-create", response_class=HTMLResponse)
async def order_create(order: OrderModel):
    order = OrderModel(
        customer_name = order.customer_name,
        customer_email = order.customer_email,
        items = order.items,
        usecase = Depends(get_order_usecase),
    )
    await uc_order_form.create_order(order)
    return RedirectResponse("/order-create", status_code=201)
