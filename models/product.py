from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str]
    created_at: Optional[str]
    name: str
    image_url: str
    brand: str
    unit: str