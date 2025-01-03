from typing import Optional
from pydantic import BaseModel
from models.product import Product
from models.store import Store


class Price(BaseModel):
    id: Optional[str]
    created_at: Optional[str]
    product_id: str
    store_id: str
    product: Optional[Product]
    store: Optional[Store]
    price: float
    unit: str
