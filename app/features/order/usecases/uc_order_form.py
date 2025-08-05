from app.features.order.models.order_model import OrderModel
from app.features.order.repositories.interface import OrderRepository

class OrderFormUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    async def create_order(self, order: OrderModel):
        return await self.repo.save(order)
