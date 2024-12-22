from typing import Optional
from pydantic import BaseModel

class Price(BaseModel):
    id: Optional[str]
    created_at: Optional[str]
    product_id: str
    store_id: str
    price: float
    unit: str
