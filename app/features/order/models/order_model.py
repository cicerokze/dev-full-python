from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, EmailStr, Field, model_validator
from datetime import datetime
from typing import Annotated, Optional
from app.features.order.models.item_model import OrderItemModel

PyObjectId = Annotated[str, BeforeValidator(str)]

# Schema para definição de Pedido
class OrderModel(BaseModel):
    """
    Container for a single order record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    customer_name: str = Field(..., description="Name of the customer placing the order")
    customer_email: EmailStr = Field(..., description="Email address of the customer")
    items: list[OrderItemModel] = Field(..., description="List of items in the order")
    price: float = Field(..., description="Total price of the order")
    date: datetime = Field(..., description="Date and time when the order was placed")
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "customer_name": "John Doe",
                "customer_email": "jdoe@example.com",
                "items": [
                    {
                        "item_id": "60c72b2f9b1e8b001c8e4d1a",
                        "name": "Item 1",
                        "category": "Category 1",
                        "quantity": 2,
                        "unit_price": 10.0
                    },
                    {
                        "item_id": "60c72b2f9b1e8b001c8e4d1b",
                        "name": "Item 2",
                        "category": "Category 2",
                        "quantity": 1,
                        "unit_price": 11.0
                    }
                ],
                "price": 31.0,
                "date": "2024-01-19T00:00:00Z"
            }
        }
    )

    @model_validator(mode='before')
    def check_price(cls, values):
        price = values.get('price')
        if price is None:
            values['price'] = 0.0  # Default to 0.0 if None
        return values

class UpdateOrderModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    customer_name: Optional[str] = None
    customer_email: Optional[EmailStr] = None
    items: Optional[list[OrderItemModel]] = None
    price: Optional[float] = None
    date: Optional[datetime] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "customer_name": "John Doe",
                "customer_email": "jdoe@example.com",
                "items": [
                    {
                        "item_id": "60c72b2f9b1e8b001c8e4d1a",
                        "name": "Item 1",
                        "category": "Category 1",
                        "quantity": 2,
                        "price": 10.0
                    },
                    {
                        "item_id": "60c72b2f9b1e8b001c8e4d1b",
                        "name": "Item 2",
                        "category": "Category 2",
                        "quantity": 1,
                        "price": 11.0
                    }
                ],
                "price": 31.0,
                "date": "2024-01-19T00:00:00Z"
            }
        }
    )

    @model_validator(mode='before')
    def check_price(cls, values):
        price = values.get('price')
        if price is None:
            values['price'] = 0.0  # Default to 0.0 if None
        return values

class OrderCollection(BaseModel):
    """
    A container holding a list of `OrderModel` records.
    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """
    orders: list[OrderModel]