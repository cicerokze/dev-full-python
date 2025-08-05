from bson import ObjectId
from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from pymongo import ReturnDocument
from app.core.database import orders_collection
from app.features.order.models.order_model import OrderModel

api_order_form_router = APIRouter()

@api_order_form_router.post(
    "/orders/",
    response_description="Add a new order",
    response_model=OrderModel,
    status_code=201,
    response_model_by_alias=False,
)
async def create_order(order: OrderModel = Body(...)):
    """
    Insert a new order record.
    A unique `id` will be created and provided in the response.
    """
    new_order = await orders_collection.insert_one(
        order.model_dump(by_alias=True, exclude=["id"])
    )
    created_order = await orders_collection.find_one(
        { "_id": new_order.inserted_id }
    )
    return created_order

@api_order_form_router.put(
    "/orders/{id}",
    response_description="Update an order",
    response_model=OrderModel,
    response_model_by_alias=False,
)
async def update_order(id: str, order: OrderModel = Body(...)):
    """
    Update an existing order by its `id`.
    """
    order = {
        k: v for k, v in order.model_dump(by_alias=True).items() if v is not None
    }
    
    if len(order) >= 1:
        update_result = await orders_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": order},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Order {id} not found")
    
    # The update is empty, but we should still return the matching document:
    if (existing_order := await orders_collection.find_one({"_id": id})) is not None:
        return existing_order

    raise HTTPException(status_code=404, detail=f"Order {id} not found")