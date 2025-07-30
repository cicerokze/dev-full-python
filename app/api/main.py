from fastapi import APIRouter

api_router = APIRouter()

# Orders API endpoints
@api_router.get("/orders")
async def list_orders():
    # Return JSON with orders (replace with real logic)
    return [{"id": 1, "customer_name": "Alice"}]

@api_router.post("/orders")
async def create_order(order: dict):
    # Create order logic here
    return {"msg": "Order created", "order": order}