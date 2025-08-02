from abc import ABC, abstractmethod
from app.features.order.models.order_model import OrderModel

class OrderRepository(ABC):
    @abstractmethod
    async def save(self, order: OrderModel):
        pass
