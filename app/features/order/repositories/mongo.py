import re
from datetime import datetime
from app.core.database import db
from app.features.order.models.order_model import OrderModel
from app.features.order.repositories.interface import OrderRepository

class MongoOrderRepository(OrderRepository):
    async def save(self, order: OrderModel):
        order_dict = order.model_dump()
        return await db.orders.insert_one(order_dict)

    async def list_paginated(self, page: int, filters: dict):
        page_size = 10
        query = {}

        if filters["customer_name"]:
            query["customer_name"] = {"$regex": re.escape(filters["customer_name"]), "$options": "i"}
        if filters["start_date"] and filters["end_date"]:
            query["order_date"] = {
                "$gte": datetime.fromisoformat(filters["start_date"]),
                "$lte": datetime.fromisoformat(filters["end_date"])
            }

        total = await db.orders.count_documents(query)
        cursor = db.orders.find(query).skip((page - 1) * page_size).limit(page_size)
        orders = await cursor.to_list(length=page_size)

        return {
            "orders": orders,
            "total_pages": (total + page_size - 1) // page_size
        }
