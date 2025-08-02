from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import Annotated, List, Optional

from app.features.order.models.item_model import ItemModel

PyObjectId = Annotated[str, BeforeValidator(str)]

# Schema para definição de Pedido
class OrderModel(BaseModel):
    """
    Container for a single order record.
    """

    order_id: Optional[PyObjectId] = Field(alias="_id", default=None)
    customer_name: str 
    customer_email: EmailStr
    items: List[ItemModel]
    datetime: datetime
    price: float
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "customer_name": "John Doe",
                "customer_email": "jdoe@example.com",
                "items": [
                    {
                        "name": "Item 1",
                        "quantity": 2,
                        "price": 10.0
                    },
                    {
                        "name": "Item 2",
                        "quantity": 1,
                        "price": 11.0
                    }
                ],
                "datetime": "2023-10-01T12:00:00Z",
                "price": 31.0
            }
        }
    )

class UpdateOrderModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    customer_name: Optional[str] = None
    customer_email: Optional[EmailStr] = None
    items: Optional[List[ItemModel]] = None
    datetime: Optional[float] = datetime
    price: Optional[float] = items
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "customer_name": "John Doe",
                "customer_email": "jdoe@example.com",
                "items": [
                    {
                        "name": "Item 1",
                        "quantity": 2,
                        "price": 10.0
                    },
                    {
                        "name": "Item 2",
                        "quantity": 1,
                        "price": 11.0
                    }
                ],
                "datetime": "2023-10-01T12:00:00Z",
                "price": 31.0
            }
        }
    )

class OrderCollection(BaseModel):
    """
    A container holding a list of `OrderModel` instances.
    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """
    orders: List[OrderModel]