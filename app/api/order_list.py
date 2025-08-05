from bson import ObjectId
from fastapi import APIRouter, HTTPException, Response
from app.features.order.models.order_model import OrderCollection, OrderModel
from app.core.database import orders_collection

api_order_list_router = APIRouter()

@api_order_list_router.get(
    "/orders/",
    response_description="List all orders",
    response_model=OrderCollection,
    response_model_by_alias=False,
)
async def list_orders():
    """
    List all of the orders data in the database.
    The response is unpaginated and limited to 10 results.
    """
    if not (orders := await orders_collection.find().to_list(10)):
        raise HTTPException(status_code=404, detail="No orders found")
    
    return OrderCollection(orders = await orders_collection.find().to_list(10))

@api_order_list_router.get(
    "/orders/{id}",
    response_description="Get a single order",
    response_model=OrderModel,
    response_model_by_alias=False,
)
async def show_order(id: str):
    """
    Retrieve a single order by its `id`.
    """
    if (
        order := await orders_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return order
    
    raise HTTPException(status_code=404, detail=f"Order {id} not found")

@api_order_list_router.delete(
    "/orders/{id}",
    response_description="Delete an order",
)
async def delete_order(id: str):
    """
    Delete an existing order by its `id`.
    """
    delete_result = await orders_collection.delete_one({"_id": ObjectId(id)})
    
    if delete_result.deleted_count == 1:
        return Response(status_code=204)
    
    raise HTTPException(status_code=404, detail=f"Order {id} not found")