from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]
# Schema para definição de Item
class ItemModel(BaseModel):
    """
    Container for a single item record.
    """

    item_id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    category: str
    unit_price: float
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Item 1",
                "category": "Category A",
                "unit_price": 10.0
            }
        }
    )