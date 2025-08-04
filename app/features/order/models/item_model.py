from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, model_validator
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]

class ItemModel(BaseModel):
    """
    Container for a single item record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(..., description="Name of the item")
    category: str = Field(..., description="Category of the item")
    unit_price: float = Field(..., description="Unit price of the item")
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "60c72b2f9b1e8b001c8e4d1a",
                "name": "Item 1",
                "category": "Category A",
                "unit_price": 10.0
            }
        }
    )

    @model_validator(mode='before')
    def check_unit_price(cls, values):
        unit_price = values.get('unit_price')
        if unit_price is None:
            values['unit_price'] = 0.0  # Default to 0.0 if None
        return values

class UpdateItemModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    name: Optional[str] = None
    category: Optional[str] = None
    unit_price: Optional[float] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "name": "Updated Item",
                "category": "Updated Category",
                "unit_price": 12.0
            }
        }
    )

    @model_validator(mode='before')
    def check_unit_price(cls, values):
        unit_price = values.get('unit_price')
        if unit_price is None:
            values['unit_price'] = 0.0  # Default to 0.0 if None
        return values

# Schema para definição de Item
class OrderItemModel(ItemModel):
    """
    Container for a single item record.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(..., description="Name of the item")
    category: str = Field(..., description="Category of the item")
    unit_price: float = Field(..., description="Unit price of the item")
    quantity: int = Field(..., description="Quantity of the item in the order")
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "60c72b2f9b1e8b001c8e4d1a",
                "name": "Item 1",
                "category": "Category A",
                "quantity": 2,
                "unit_price": 10.0
            }
        }
    )

    @model_validator(mode='before')
    def check_unit_price(cls, values):
        unit_price = values.get('unit_price')
        if unit_price is None:
            values['unit_price'] = 0.0  # Default to 0.0 if None
        return values

class UpdateOrderItemModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    name: Optional[str] = None
    category: Optional[str] = None
    unit_price: Optional[float] = None
    quantity: Optional[int] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "name": "Updated Item",
                "category": "Updated Category",
                "unit_price": 12.0
            }
        }
    )

    @model_validator(mode='before')
    def check_unit_price(cls, values):
        unit_price = values.get('unit_price')
        if unit_price is None:
            values['unit_price'] = 0.0  # Default to 0.0 if None
        return values

class ItemCollection(BaseModel):
    """
    Container for a list of item records.
    """

    items: list[ItemModel]

class OrderItemCollection(OrderItemModel):
    """
    Container for a list of item records.
    """

    items: list[OrderItemModel]
    