from typing import Optional
from pydantic import BaseModel

class Store(BaseModel):
    id: Optional[str]
    created_at: Optional[str]
    name: str
