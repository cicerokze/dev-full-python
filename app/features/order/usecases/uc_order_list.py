from typing import Dict
from app.features.order.repositories.interface import OrderRepository

class OrderListUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    async def list_orders(self, page: int, filters: Dict):
        return await self.repo.list_paginated(page=page, filters=filters)
